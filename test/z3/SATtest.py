from z3 import *

graph = {}
bool_dict = {}
bool_graph = {}

var01 = 'xtsgndp'
val11 = (1,2,3,4,5,6)
val12 = (1,2,4,4,5,6)

var02 = 'xtsgnd'
val21 = (1,2,3,4,5)
val22 = (1,2,4,4,5)

graph = {
	var01 : {
		val11 : [(var02,val21),('or',[(var01,val11),(var01,val12)])],
		val12 : [(var02,val22)]
	},
	var02 : {
		val21 : [(var01,val11),('and',[(var02,val21),(var01,val12)])],
		val22 : [(var01,val12)]
	}
}

#nvars = [len(graph[i]) for i in graph]
#cvars = [[(i,j) for j in (graph[i])] for i in graph]

def pf(i, j):		#pretty function
	return '(' + str(i) + ', ' + str(j) + ')'

def ParseVal(v):		#string to bool parser
	if(v[0] == 'or'):
		return Or([bool_dict[b] for b in v[1]])
	elif(v[0] == 'and'):
		return And([bool_dict[b] for b in v[1]])
	else:
		return bool_dict[v]

for i in graph:			#z3 bool instance dict
	for j in graph[i]:
		bool_dict[(i,j)] = Bool(pf(i, j))

#print bool_dict

for i in graph:			#z3 bool instance clause dict
	for j in graph[i]:
		bool_graph[bool_dict[(i,j)]] = [ParseVal(v) for v in graph[i][j]]

#print bool_graph

def DependsOn(pack, deps):
    return And([ Implies(pack, dep) for dep in deps ])

#dvars = []
#k = 0

#for i in nvars:
#	for j in range(i):
#		dvars.append(cvars[k][j])
#	k = k + 1
#

#for i in range(len(dvars)):
#	dvars[i] = Bool(str(dvars[i]))

sol_list = []

for i in bool_graph:
	sol_list.append(DependsOn(i,bool_graph[i]))

solve(sol_list)

#print type(dvars)
#print type(dvars[1])
#for i in range(len(cvars))
