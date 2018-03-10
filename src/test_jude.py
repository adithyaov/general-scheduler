import numpy as np
from cons.py import *
from var.py import *

graph = {}

num_t = 10
num_s = 10
num_g = 10
num_d = 6
teachers = np.array(range(num_t))
subjects = np.array(range(num_s))
groups = np.array(range(num_g))
n_max = 4
days = range(num_d)
periods = []
for _ in days:
    periods.append([0, 1, 2, 3, 4, 5])

'''
periods[2] = [0, 1, 2, 3, 4, 5] => 6 periods
'''

'''
duration[t, s, g, n] = 2
'''

# Make zeros and change later, but this is test file, so whatever
duration = np.zeros([num_t, num_s, num_g, n_max])
duration[0, 0, 0, 0] = 1
duration[1, 1, 1, 1] = 1
'''
node can be representated as ('x', t, s, g, n, d, p)
graph will be the same but these tuples as nodes
'''


def bic1(t, s, g, n, d, p1, p2):
    truth = [
        (p1 > np.min(periods[d])),
        (p1 <= np.max(periods[d]) - duration[t, s, g, n] + 1),
        (p2 >= p1),
        (p2 <= p1 + duration[t, s, g, n] - 1)
    ]
    return np.prod(truth)


def bic2(t, s, g, n, d, p1, p2):
    truth = [
        (p1 <= p2),
        (p1 >= p2 - duration[t, s, g, n] + 1),
        (p1 >= np.min(periods[d])),
        (p1 <= np.max(periods[d]) - duration[t, s, g, n] + 1)
    ]
    return np.prod(truth)


def bic3(d, p):
    truth = [
        (p <= np.max(periods[d])),
        (p >= np.min(periods[d]))
    ]
    return np.prod(truth)


def bic4(d, p):
    truth = [
        (p in periods[d])
    ]
    return np.prod(truth)


def bic5(t, s, g, n, d, p):
    truth = [
        (p1 >= np.min(periods[d])),
        (p1 <= np.max(periods[d]) - duration[t, s, g, n] + 1)
    ]
    return np.prod(truth)


def bic6(t, s, g, n):
    # this means tsgn belongs to lessons[t] and to lessons[g]
    truth = [
        (duration[t, s, g, n] > 0)
    ]
    return np.prod(truth)


def bic7(d):
    truth = [
        (d in days)
    ]
    return np.prod(truth)


def bic8(k, d):
    truth = [
        (k >= 1),
        (k <= len(periods[d]) - 2),
        (p >= np.min(periods[d]) + 1),
        (p <= np.max(periods[d]) - k)
    ]
    return np.prod(truth)


def bic9(k, d):
    truth = [
        (k >= 1),
        (k <= len(periods[d]) - 2)
    ]
    return np.prod(truth)


def bic10(k, d):
    truth = [
        (p >= np.min(periods[d]) + 1),
        (p <= np.max(periods[d]) - k)
    ]
    return np.prod(truth)


def bic11(d, p):
    truth = [
        (p >= np.min(periods[d]) + 1),
        (p <= np.max(periods[d]) - 1)
    ]
    return np.prod(truth)


def bic11(k, d, p):
    truth = [
        (k >= 1),
        (k <= np.max(periods[d]) - p)
    ]
    return np.prod(truth)


for t in teachers:
    for s in subjects:
        for g in groups:
            for n in range(n_max):
                if (duration[t, s, g, n] > 0):  # Valid lesson
                    for d in days:
                        graph[('xtd', t, d)] = []
                        graph[('xtsgnd', t, s, g, n, d)] = []
                        for p in periods[d]:
                            graph[('xtp', t, p)] = []
                            graph[('xtdp', t, d, p)] = []
                            graph[('xgdp', g, d, p)] = []
                            if np.min(periods[d]) <= p and p <= max(periods[d] - duration[t, s, g, n] + 1):
                                graph[('x!tsgnd', t, s, g, n, d, p)] = []
                                graph[('xtsgnd', t, s, g, n, d, p)] = []


for t in teachers:
    for d in days:
        for p in periods[p]:
            for k in range(len(periods[p])):
                if k >= 1 and k <= len(periods[p]) - 2:
                    if p >= np.min(periods[d]) + 1 and p <= np.max(periods[d]) - k:
                        graph[('iktdp', k, t, d, p)] = []
                        graph[('iktd', k, t, d)] = []

for g in groups:
    for d in days:
        for p in periods[p]:
            for k in range(len(periods[p])):
                if k >= 1 and k <= len(periods[p]) - 2:
                    if p >= np.min(periods[d]) + 1 and p <= np.max(periods[d]) - k:
                        graph[('ikgdp', k, g, d, p)] = []
                        graph[('ikgd', k, g, d)] = []

print(len(graph.keys()))


'''
graph[('x', t, s, g, n, d, p)] = [('or', [...])]
'''

# Correctness constraints

for (t, s, g, n) in duration.keys():
    or_list = []
    for d in days:
        or_list.append(('xtsgnd', t, s, g, n, d))
    true_list.append(('or', or_list))


multi_dict = {}
for (t, s, g, n) in duration.keys():
    multi_dict[(t, s, g, n)] = []
for (t, s, g, n, d) in graph2['xtsgnd'].keys():
    multi_dict[(t, s, g, n)].append(('xtsgnd', t, s, g, n, d))
for (t, s, g, n) in multi_dict.keys():
    true_list.append(single(multi_dict[(t, s, g, n)]))

multi_dict = {}
for (t, s, g, n, d, p) in graph2['x!tsgndp'].keys():
    multi_dict[(t, s, g, n, d)] = []
for (t, s, g, n, d, p) in graph2['x!tsgndp'].keys():
    multi_dict[(t, s, g, n, d)].append(('x!tsgndp', t, s, g, n, d, p))
for (t, s, g, n, d) in multi_dict.keys():
    true_list.append(single(multi_dict[(t, s, g, n, d)]))


multi_dict = {}
for (t, s, g, n, d, p) in graph2['xtsgndp'].keys():
    multi_dict[(g, d, p)] =  []
for (t, s, g, n, d, p) in graph2['xtsgndp'].keys():
    multi_dict[(g, d, p)].append(('xtsgndp', t, s, g, n, d, p))
for (g, d, p) in multi_dict.key():
    true_list.append(single(multi_dict[(g, d, p)]))
    