from collections import defaultdict
import var
# 1) Forbidden and requested working hours

if not teacher_forbidden0:
    for (t, d, p) in teacher_forbidden0:
        comfort_true_list.append(negation(('xtdp', (t, d, p))))

if not teacher_forbidden1:
    for (t, d) in teacher_forbidden1:
        comfort_true_list.append(negation(('xtd', (t, d))))

if not teacher_forbidden2:
    for (t, p) in teacher_forbidden2:
        comfort_true_list.append(negation(('xtp', (t, p))))

if not teacher_requested0:
    for (t, d, p) in teacher_requested0:
        comfort_true_list.append(('xtdp', (t, d, p)))

if not teacher_requested1:
    for (t, d) in teacher_requested1:
        comfort_true_list.append(('xtd', (t, d)))

if not teacher_requested2:
    for (t, p) in teacher_requested2:
        comfort_true_list.append(('xtp', (t, p)))

if not group_forbidden0:
    for (g, d, p) in group_forbidden0:
        comfort_true_list.append(negation(('xgdp', (g, d, p))))

if not group_forbidden1:
    for (g, d) in group_forbidden1:
        comfort_true_list.append(negation(('xgd', (g, d))))

if not group_forbidden2:
    for (g, p) in group_forbidden2:
        comfort_true_list.append(negation(('xgp', (g, p))))

if not group_requested0:
    for (g, d, p) in group_requested0:
        comfort_true_list.append(('xgdp', (g, d, p)))

if not group_requested1:
    for (g, d) in group_requested1:
        comfort_true_list.append(('xgd', (g, d)))

if not group_requested2:
    for (g, p) in group_requested2:
        comfort_true_list.append(('xgp', (g, p)))


# 2) Avoiding groups and teachers overlapping

if not teacher_no_overlap:
    for (t1, t2) in teacher_no_overlap:
        for d in days:
            for p in periods[d]:
                comfort_graph['xtdp'][(t1, d, p)].append(
                    negation(('xtdp', (t2, d, p))))
                comfort_graph['xtdp'][(t2, d, p)].append(
                    negation(('xtdp', (t1, d, p))))

if not group_no_overlap:
    for (g1, g2) in group_no_overlap:
        for d in days:
            for p in periods[d]:
                comfort_graph['xgdp'][(g1, d, p)].append(
                    negation(('xgdp', (g2, d, p))))
                comfort_graph['xgdp'][(g2, d, p)].append(
                    negation(('xgdp', (g1, d, p))))

# 3) Number of teaching days for a teacher

if not teaching_days:
    for (t, n) in teaching_days:
        atmost_var_list = []
        atleast_var_list = []
        for d in days:
            atmost_var_list.append(('xtd', (t, d)))
            atleast_var_list.append(negation(('xtd', (t, d))))

        atmost_n = Cardinality(atmost_var_list, n)
        comfort_true_list.append(atmost_n.form())

        atleast_n = Cardinality(atleast_var_list, (no_of_days - n))
        comfort_true_list.append(atleast_n.form())

# 4) Work day duration: ('xgdp' ∧ 'xgd(p+k−1)') => 'lkgd' min(periods(d)) <= p <= max(periods(d)) - k + 1
#                     ('lkgd' => (or, ('xgdp' ^ 'xgd(p+k-1)')) min(periods(d)) <= p  <= max(periods(d)) - k+1

#                     also for every working day: 'xgd' => 'lkgd'
#                     atmost n hours:  negation('lkgd') for all k > n

if not work_day_duration:
    for (g, k, d) in work_day_duration:
        comfort_graph['lkgd'][(g, k, d)] = []

        or_list = []
        for p in range(min(periods[d]), max(periods[d]) - k + 2):
            or_list.append(
                ('and', [('xgdp', (g, d, p)), ('xgdp', (g, d, p + k - 1))]))
            comfort_true_list.append(('or', [negation(('xgdp', (g, d, p))), negation(
                ('xgdp', (g, d, p + k - 1))), ('lkgd', (k, g, d))]))

        comfort_graph['lkgd'][(g, k, d)].append(('or', or_list))

# Atmost n hours on day d for group g

if not duration_upper_limit:
    for (g, d, n) in duration_upper_limit:
        for k in range(n + 1, max(periods[d]) + 1): # DOUBT ----------
            comfort_true_list.append(negation(('lkgd', (k, g, d))))

# Atleast n hours on day d for group g

if not duration_lower_limit:
    for (g, d, n) in duration_lower_limit:
        comfort_graph['xgd'][(g, d)].append(
            ('lkgd', (n, g, d)))  # Not convinced, I think you are right

# 5) Idle duration cardinality('xtgdp')

# Idle periods of length k not allowed

if not teacher_max_idle_length:
    for (t, k) in teacher_max_idle_length:
        comfort_true_list.append(negation(('ikt', (k, t))))

# Atmost one idle period for a teacher per day

if not teacher_atmost_one_idle_period:
    for t in teacher_atmost_one_idle_period:
        var_list = []
        for d in days:
            for p in range(min(periods[d]) + 1, max(periods[d]) - 1 + 1): # CHANGED
                var_list.append(('itdp', (t, d, p)))

        comfort_true_list.append(single(var_list))

# Atmost k idle periods for a teacher in a week

if not teacher_atmost_k_idle_period:
    for (t, k) in teacher_atmost_k_idle_period:
        var_list = []
        for d in days:
            for p in periods[d]:
                var_list.append(('itdp', (t, d, p)))

        atmost_k = Cardinality(var_list, k)
        comfort_true_list.append(atmost_k.form())

# For groups
# Idle periods of length k not allowed

if not group_max_idle_length:
    for (g, k) in group_max_idle_length:
        comfort_true_list.append(negation(('ikg', (k, g))))

# Atmost one idle period for a group per day

if not group_atmost_one_idle_period:
    for g in group_atmost_one_idle_period:
        var_list = []
        for d in days:
            for p in range(min(periods[d]) + 1, max(periods[d]) - 1 + 1): # CHANGED
                var_list.append(('igdp', (g, d, p)))

        comfort_true_list.append(single(var_list))

# Atmost k idle periods for a teacher in a week

if not group_atmost_k_idle_period:
    for (g, k) in group_atmost_k_idle_period:
        var_list = []
        for d in days:
            for p in periods[d]:
                var_list.append(('igdp', (g, d, p)))

        atmost_k = Cardinality(var_list, k)
        comfort_true_list.append(atmost_k.form())

# 6) Forbidden hours and requested hours:
# Favoured periods: 'xtsgnd' => 'x!tsgndp1' or ...

if not favoured_hours:  # dict = {(t,s,g,n):[p]}
    confort_graph['xtsgnd'] = defaultdict(lambda: [])
    for (t, s, g, n) in favoured_hours.keys():
        for d in days:
            comfort_graph['xtsgnd'][(t, s, g, n, d)] = []
            or_list = []
            for p in favoured_hours[(t,s,g,n)]:
                if bic3(d, p):
                    or_list.append(('x!tsgndp', (t, s, g, n, d, p)))
    
            comfort_graph['xtsgnd'][(t, s, g, n, d)].append(('or', or_list))

#first or last last lesson in a day: 'x!tsgndp' => (and, negation('xgdp')) or ('and', negation('xgdp'))

if not last_first_hours:
    for (t, s, g, n) in last_first_hours:
        for d in days:
            for p in periods[d]:
                comfort_graph['x!tsgndp'][(t, s, g, n, d, p)] = []
                and_list1 = []
                for p2 in range(min(periods[d]), p): # CHANGED
                    and_list1.append(negation(('xgdp', (g, d, p2))))

                and_list2 = []
                for p2 in range(p + duration[(t, s, g, n)], max(periods(d) + 1)):
                    and_list2.append(negation(('xgdp', (g, d, p))))

                or_list = [('and', and_list1), ('and', and_list2)]
    
                comfort_graph['x!tsgndp'][(t, s, g, n, d, p)].append(('or', or_list))


# 7) lessons on non consecutive days:
#   'xtsgnd' => negation('xtsg(n + 1)(d+1))
#   except for last working day

if not non_consecutive:
    for (t, s, g, n) in non_consecutive:
        for d in days[:-1]:
            comfort_graph['xtsgnd'][(t, s, g, n, d)].append(negation(('xtsgnd', (t, s, g, n + 1, d + 1))))


