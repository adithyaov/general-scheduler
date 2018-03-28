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
