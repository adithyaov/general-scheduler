import numpy as np

from var import *
from cons import *

# initializing vars


for (t, s, g, n) in duration.keys():
	for d in days:
		graph[('xtsgnd', t, s, g, n, d)] = []
		for p in periods[d]:
			graph[('x!tsgndp', t, s, g, n, d, p)] = []
			graph[('xtsgndp', t, s, g, n, d, p)] = []


for t in teachers:
	for d in days:
		graph[('xtd', t, d)] = []
		for p in periods[d]:
			graph[('xtdp', t, d, p)] = []

for t in teachers:
	for p in range(p_max):
		graph[('xtp', t, p)] = []

for g in groups:
	for d in days:
		for p in periods[d]:
			graph[('xgdp', g, d, p)] = []


for k in range(p_max):
	for t in teachers:
		graph[('ikt', k, t)] = []
		for d in days:
			if bic9(k, d):
				graph[('iktd', k, t, d)] = []
			for p in periods[p]:
				if bic8(k, d, p):
					graph[('iktdp', k, t, d, p)] = []

for k in range(p_max):
	for g in groups:
		graph[('ikg', k, g)] = []
		for d in days:
			if bic9(k, d):
				graph[('ikgd', k, g, d)] = []
			for p in periods[p]:
				if bic8(k, d, p):
					graph[('ikgdp', k, g, d, p)] = []


for t in teachers:
	for d in days:
		for p in periods[d]:
			if bic11(d, p):
				graph[('itdp', t, d, p)] = []

for g in groups:
	for d in days:
		for p in periods[d]:
			if bic11(d, p):
				graph[('igdp', g, d, p)] = []


# Implications

for (t, s, g, n) in duration.keys():
	for d in days:
		for p1 in periods[d]:
			for p2 in periods[d]:
				if bic1(t, s, g, n, d, p1, p2):
					graph[('x!tsgndp', t, s, g, n, d, p1)].append(('xtsgndp', t, s, g, n, d, p2))

for (t, s, g, n) in duration.keys():
	for d in days:
		for p2 in periods[d]:
			if bic3(d, p2):
				or_list = []
				for p1 in periods[d]:
					if bic2(t, s, g, n, d, p1, p2):
						or_list.append(('x!tsgndp', t, s, g, n, d, p1))
				graph[('xtsgndp', t, s, g, n, d, p2)].append(('or', or_list))


for (t, s, g, n) in duration.keys():
	for d in days:
		or_list = []
		for p in periods[d]:
			graph[('xtsgndp', t, s, g, n, d, p)].append(('xtsgnd', t, s, g, n, d))
			graph[('xtsgndp', t, s, g, n, d, p)].append(('xtdp', t, d, p))
			graph[('xtsgndp', t, s, g, n, d, p)].append(('xgdp', g, d, p))
			or_list.append(('xtsgndp', t, s, g, n, d, p))
		graph[('xtsgnd', t, s, g, n, d)].append(('or', or_list))

'''
Can modify the below two loops to make it more efficient
'''

for t in teachers:
	for (t, s, g, n) in lessons_t[t]:
		or_list = []
		for d in days:
			for p in periods[d]:
				or_list.append(('xtsgndp', t, s, g, n, d, p))
	graph[('xtdp', t, d, p)].append(('or', or_list))


for g in groups:
	for (t, s, g, n) in lessons_g[g]:
		or_list = []
		for d in days:
			for p in periods[d]:
				or_list.append(('xtsgndp', t, s, g, n, d, p))
	graph[('xgdp', t, d, p)].append(('or', or_list))


for t in teachers:
	for d in days:
		or_list = []
		for p in periods[d]:
			or_list.append(('xtdp', t, d, p))
			graph[('xtdp', t, d, p)].append(('xtd', t, d))
		graph[('xtd', t, d)].append(('or', or_list))


for t in teachers:
	for p in range(p_max):
		or_list = []
		for d in days:
			if bic13(d, p):
				or_list.append(('xtdp', t, d, p))
				graph[('xtdp', t, d, p)].append(('xtd', t, d))
		graph[('xtp', t, p)].append(('or', or_list))




for k in range(p_max):
	for t in teachers:
		for d in days:
			for p in periods[p]:
				if bic8(k, d, p):
					or_list = []
					graph[('iktdp', k, t, d, p)].append(('xtdp', t, d, p - 1))
					for j in range(k):
						graph[('iktdp', k, t, d, p)].append(('~xtdp', t, d, p + j))
						or_list.append(('xtdp', t, d, p + j))
					graph[('iktdp', k, t, d, p)].append(('xtdp', t, d, p + k))
					true_list.append(
						('or', [
							('~xtdp', t, d, p - 1), 
							('or', or_list), 
							('~xtdp', t, d, p + k),
							('~iktdp', k, t, d, p)
						]))

for k in range(p_max):
	for t in teachers:
		for d in days:
			or_list = []
			for p in periods[p]:
				if bic8(k, d, p):
					graph[('iktdp', k, t, d, p)].append(('iktd', k, t, d))
				if bic10(k, d, p):
					or_list.append(('iktdp', k, t, d, p))
			if bic9(k, d):
				graph[('iktd', k, t, d)].append(('or', or_list))

for k in range(p_max):
	for t in teachers:
		or_list = []
		for d in days:
			if bic9(k, d):
				graph[('iktd', k, t, d)].append(('ikt', k, t))
				or_list.append(('iktd', k, t, d))
		graph[('ikt', k, t)].append(('or', or_list))

for t in teachers:
	for d in days:
		for p in periods[d]:
			or_list = []
			for k in range(p_max):
				if bic12(k, d, p) and bic8(k, d, p):
					graph[('iktdp', k, t, d, p)].append(('itdp', t, d, p))
					or_list.append(('iktdp', k, t, d, p))
			if bic11(d, p):
				graph[('itdp', t, d, p)].append(('or', or_list))





print(len(graph.keys()))
# for x in graph.keys():
# 	print(x, '=>' ,graph[x])


'''
graph[('x', t, s, g, n, d, p)] = [('or', [...])]
'''


