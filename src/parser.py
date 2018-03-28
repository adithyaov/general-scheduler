from z3 import *
from test_diff_loop import *

var_result = {}				#stores result in Bool instance
sol_list = []
truth_dict = {}
bool_graph = {}

def ParseVal(v):
	if(v[0] == 'not'):
		return Not(Bool(str(v[1])))
	elif(v[0] == 'or'):
		return Or([ ParseVal(b) for b in v[1] ])					 
	elif(v[0] == 'and'):
		return And([ ParseVal(b) for b in v[1] ])
	else:
		return Bool(str(v))
	
def makeTT(*args, **keywords):		#Time table SAT solver
	s = Solver()
	s.set(**keywords)
	s.add(*args)
	if keywords.get('show', False):
		print s
	r = s.check()
	if r == unsat:
		return (False, 'No Solution')
	elif r == unknown:
		return (False, 'Failed to solve')
	else:
		return (True, s.model())

for i in graph:						#z3 bool instance clause dict
    for j in graph[i]:
    	sol_list.append(Implies(ParseVal((i, j)), ParseVal(graph[i][j])))

sol_list.append(Implies(True, ParseVal(true_list))) 	#True_list expr

time_table = makeTT(sol_list)

if time_table[0] == False:
	exit(0)

m = time_table[1]

for x in m.decls():
	var_result[x] = bool(m[x])

result_graph = {}

for x in var_result:
	y = str(x)[2:-1].split('\', ')
	result_graph[y[0]] = {
		True: [],
		False: []
	}
	
for x in var_result:
	y = str(x)[2:-1].split('\', ')
	result_graph[y[0]][var_result[x]].append(tuple(map(int, y[1][1:-1].split(','))))

