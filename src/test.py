import numpy as np

graph = {}

num_t = 10
num_s = 10
num_g = 10
teachers = np.array(range(num_t))
subjects = np.array(range(num_s))
groups = np.array(range(num_g))
n_max = 4
days = range(6)
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
duration = np.ones([num_t, num_s, num_g, n_max])

'''
node can be representated as ('x', t, s, g, n)
graph will be the same but these tuples as nodes
'''

for t in teachers:
	for s in subjects:
		for g in groups:
			for n in range(n_max):
				if (duration[t, s, g, n] > 0): # Valid lesson
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


