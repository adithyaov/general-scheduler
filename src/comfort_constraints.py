# 1) Forbidden and requested working hours:  i)  negation('xtdp') 
#                                         ii)  negation('xtd' )
#                                        iii)  negation('xtp')

teacher_forbidden0 = [(t, d, p)]
teacher_forbidden1 = [(t, d)]
teacher_forbidden2 = [(t, p)]

for (t, d, p) in teacher_forbidden0:
    comfort_true_list.append(negation(('xtdp', (t, d, p))))

for (t, d) in teacher_forbidden1:
    comfort_true_list.append(negation(('xtd', (t, d))))

for (t, p) in teacher_forbidden0:
    comfort_true_list.append(negation(('xtp', (t, p))))

for (t, d, p) in teacher_fixed0:
    comfort_true_list.append(('xtdp', (t, d, p)))

for (t, d) in teacher_fixed1:
    comfort_true_list.append(('xtd', (t, d)))

for (t, p) in teacher_fixed2:
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

for (g, d, p) in group_fixed0:
    comfort_true_list.append(('xgdp', (g, d, p)))

for (g, d) in group_fixed1:
    comfort_true_list.append(('xgd', (g, d)))

for (g, p) in group_fixed2:
    comfort_true_list.append(('xgp', (g, p)))


# 2) Groups and teachers overlapping: ('xgdp', (1, d, p)) => negation('xgdp', (2, d, p))
#                                   ('xgdp', (2, d, p)) => negation('xgdp', (1, d, p))

#                                   ('xtdp', (1, d, p)) => negation('xtdp', (2, d, p))
#                                   ('xtdp', (2, d, p)) => negation('xtdp', (1, d, p))

teacher_no_overlap = [(t1, t2)]
for (t1, t2) in teacher_no_overlap:
    for d in days:
        for p in periods[d]:
            comfort_graph['xtdp'][(t1, d, p)].append(negation(('xtdp', (t2, d, p))))
            comfort_graph['xtdp'][(t2, d, p)].append(negation(('xtdp', (t1, d, p))))

group_no_overlap = [(t1, t2)]
for (t1, t2) in teacher_no_overlap:
    for d in days:
        for p in periods[d]:
            comfort_graph['xtdp'][(t1, d, p)].append(negation(('xtdp', (t2, d, p))))
            comfort_graph['xtdp'][(t2, d, p)].append(negation(('xtdp', (t1, d, p))))
# 3) Number of teaching days: Cardinality('xtd'|d in days) <= n & Cardinality(negation('xtd')| d in days) <= |days| - n

# 4) Work day duration: ('xgdp' ∧ 'xgd(p+k−1)') => 'lkgd' min(periods(d)) <= p <= max(periods(d)) - k + 1
#                     ('lkgd' => (or, ('xgdp' ^ 'xgd(p+k-1)')) min(periods(d)) <= p  <= max(periods(d)) - k+1

#                     also for every working day: 'xgd' => 'lkgd'
#                     atmost n hours:  negation('lkgd') for all k > n

# 5) Idle duration cardinality('xtgdp')

# 6) Forbidden hours and fixed hours:
#       favoured periods: 'xtsgnd' => 'x!tsgndp1' or ...

#       first or last last lesson in a day: 'x!tsgndp' => (and, negation('xgdp')) or ('and', negation('xgdp'))

# 7) non consecutive days:
#   'xtsgnd' => negation('xtsg(n + 1)(d+1))
#   except for last working day



