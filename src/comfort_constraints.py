comfort_graph = {}

comfort_graph['xtdp'] = {}
comfort_graph['xtd'] = {}
comfort_graph['xtp'] = {}
comfort_graph['xgdp'] = {}
comfort_graph['xgd'] = {}
comfort_graph['xgp'] = {}
comfort_graph['lkgd'] = {}


# 1) Forbidden and requested working hours

teacher_forbidden0 = [(t, d, p)]
teacher_forbidden1 = [(t, d)]
teacher_forbidden2 = [(t, p)]

for (t, d, p) in teacher_forbidden0:
    comfort_true_list.append(negation(('xtdp', (t, d, p))))

for (t, d) in teacher_forbidden1:
    comfort_true_list.append(negation(('xtd', (t, d))))

for (t, p) in teacher_forbidden0:
    comfort_true_list.append(negation(('xtp', (t, p))))

for (t, d, p) in teacher_requested0:
    comfort_true_list.append(('xtdp', (t, d, p)))

for (t, d) in teacher_requested1:
    comfort_true_list.append(('xtd', (t, d)))

for (t, p) in teacher_requested2:
    comfort_true_list.append(('xtp', (t, p)))

group_forbidden0 = [(g, d, p)]
group_forbidden1 = [(g, d)]
group_forbidden2 = [(g, p)]

for (g, d, p) in group_forbidden0:
    comfort_true_list.append(negation(('xgdp', (g, d, p))))

for (g, d) in group_forbidden1:
    comfort_true_list.append(negation(('xgd', (g, d))))

for (g, p) in group_forbidden0:
    comfort_true_list.append(negation(('xgp', (g, p))))

for (g, d, p) in group_requested0:
    comfort_true_list.append(('xgdp', (g, d, p)))

for (g, d) in group_requested1:
    comfort_true_list.append(('xgd', (g, d)))

for (g, p) in group_requested2:
    comfort_true_list.append(('xgp', (g, p)))


# 2) Avoiding groups and teachers overlapping

teacher_no_overlap = [(t1, t2)]
for (t1, t2) in teacher_no_overlap:
    for d in days:
        for p in periods[d]:
            comfort_graph['xtdp'][(t1, d, p)].append(
                negation(('xtdp', (t2, d, p))))
            comfort_graph['xtdp'][(t2, d, p)].append(
                negation(('xtdp', (t1, d, p))))

group_no_overlap = [(g1, g2)]
for (g1, g2) in group_no_overlap:
    for d in days:
        for p in periods[d]:
            comfort_graph['xgdp'][(g1, d, p)].append(
                negation(('xgdp', (g2, d, p))))
            comfort_graph['xgdp'][(g2, d, p)].append(
                negation(('xgdp', (g1, d, p))))

# 3) Number of teaching days for a teacher

teaching_days = [(t, n)]        # n <= d
no_of_days = len(days)

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

work_day_duration = [(g, k, d)]

for (g, k, d) in work_day_duration:
    comfort_graph['lkgd'][(g, k, d)] = []

    or_list = []
    for p in range(min(periods[d]), max(periods[d]) - k + 2):
        or_list.append(('and', [('xgdp', (g, d, p)), ('xgdp', (g, d, p + k - 1))]))
        comfort_true_list.append(('or', [negation(('xgdp', (g, d, p))), negation(('xgdp', (g, d, p + k - 1))), ('lkgd', (k, g, d))]))

    comfort_graph['lkgd'][(g, k, d)].append(('or', or_list))

# Atmost n hours on day d for group g 
duration_upper_limit = [(g, d, n)]

for (g, d, n) in duration_upper_limit:
    for k in range(n, max(periods[d]) + 1):
        comfort_true_list.append(negation(('lkgd', (k, g, d))))

# Atleast n hours on day d for group g
duration_lower_limit = [(g, d, n)]

for (g, d, n) in duration_lower_limit:
    for 



# 5) Idle duration cardinality('xtgdp')

# 6) Forbidden hours and requested hours:
#       favoured periods: 'xtsgnd' => 'x!tsgndp1' or ...

#       first or last last lesson in a day: 'x!tsgndp' => (and, negation('xgdp')) or ('and', negation('xgdp'))

# 7) non consecutive days:
#   'xtsgnd' => negation('xtsg(n + 1)(d+1))
#   except for last working day
