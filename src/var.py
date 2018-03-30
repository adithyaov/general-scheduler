import numpy as np

true_list = []

graph = {}
graph['x!tsgndp'] = {}
graph['xtsgndp'] = {}
graph['xtsgnd'] = {}
graph['xtdp'] = {}
graph['xgdp'] = {}
graph['xtd'] = {}
graph['xtp'] = {}
graph['iktdp'] = {}
graph['iktd'] = {}
graph['ikt'] = {}
graph['ikgdp'] = {}
graph['ikgd'] = {}
graph['ikg'] = {}
graph['itdp'] = {}
graph['igdp'] = {}

num_t = 10
num_s = 10
num_g = 10
n_max = 4
p_max = 6

teachers = np.array(range(num_t))
subjects = np.array(range(num_s))
groups = np.array(range(num_g))

days = range(6)
periods = []
for _ in days:
    periods.append([0, 1, 2, 3, 4, 5])
periods[0] = [0, 1, 2, 3]

_duration = np.ones([num_t, num_s, num_g, n_max])

'''
duration = {
    (t, s, g, n): 3
}
'''
duration = {
    (0, 0, 0, 1): 4,
    (0, 0, 1, 2): 4,
    (0, 1, 0, 2): 4,
    (0, 1, 1, 2): 4,
    (1, 0, 0, 2): 4,
    (1, 0, 1, 2): 4,
    (1, 1, 0, 2): 4,
    (1, 1, 1, 2): 4
}

'''
lessons of t
lessons_t[t] = [(t, s, g, n)]
'''

def compute_lessons():
    lessons_t = [[] for _ in range(num_t)]
    lessons_g = [[] for _ in range(num_g)]
    for x in duration.keys():
        lessons_t[x[0]].append(x)
        lessons_g[x[2]].append(x)
    return (lessons_t, lessons_g)

(lessons_t, lessons_g) = compute_lessons()



comfort_graph = {}
comfort_graph['xtdp'] = {}
comfort_graph['xtsgnd'] = {}
comfort_graph['x!tsgndp'] = {}
comfort_graph['xtd'] = {}
comfort_graph['xtp'] = {}
comfort_graph['xgdp'] = {}
comfort_graph['xgd'] = {}
comfort_graph['xgp'] = {}
comfort_graph['lkgd'] = {}

teacher_forbidden0 = [(t, d, p)]
teacher_forbidden1 = [(t, d)]
teacher_forbidden2 = [(t, p)]

teacher_requested0 = [(t, d, p)]
teacher_requested1 = [(t, d)]
teacher_requested2 = [(t, p)]

group_forbidden0 = [(g, d, p)]
group_forbidden1 = [(g, d)]
group_forbidden2 = [(g, p)]

group_requested0 = [(g, d, p)]
group_requested1 = [(g, d)]
group_requested2 = [(g, p)]

teacher_no_overlap = [(t1, t2)]

group_no_overlap = [(g1, g2)]

teaching_days = [(t, n)]        # n <= d
no_of_days = len(days)

work_day_duration = [(g, k, d)]

duration_upper_limit = [(g, d, n)]

duration_lower_limit = [(g, d, n)]

teacher_max_idle_length = [(t, k)]
teacher_atmost_one_idle_period = [t]
teacher_atmost_k_idle_period = [(t, k)]

group_max_idle_length = [(g, k)]
group_atmost_one_idle_period = [g]
group_atmost_k_idle_period = [(g, k)]

favoured_hours:  # dict = {(t,s,g,n, d):[p]}
last_first_hours #[(t,s,g,n)]