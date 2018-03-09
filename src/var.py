import numpy as np

graph = {}

num_t = 2
num_s = 2
num_g = 2
n_max = 2

teachers = np.array(range(num_t))
subjects = np.array(range(num_s))
groups = np.array(range(num_g))

days = range(6)
periods = []
for _ in days:
	periods.append([0, 1, 2, 3, 4, 5])
	
duration = np.ones([num_t, num_s, num_g, n_max])
