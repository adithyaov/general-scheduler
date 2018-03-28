from graph import *

nvars = [len(graph[i]) for i in graph]
cvars = [[(i,j) for j in (graph[i])] for i in graph]


def form_var(tup):
	var = tup[0]
	for i in range(len(tup[1])):
		var += str(tup[1][i])
	return var

and_symbol = '[and]'
or_symbol = '[or]'

def recurse_solve(formula, init_list):
	new_list = init_list
	if type(formula) == type([]):
		formula = (and_symbol, formula)
	for x in formula[1]:
		if x[0] in [and_symbol, or_symbol]:
			new_list.append('(')
			new_list = new_list + recurse_solve(x, [])
			new_list.append(')')
		else:
			var = form_var(x)
			new_list.append(var)
		new_list.append(formula[0])
	return new_list[:-1]



var01 = 'xtsgndp'
val11 = (1,2,3,4,5,6)
val12 = (1,2,4,4,5,6)

var02 = 'xtsgnd'
val21 = (1,2,3,4,5)
val22 = (1,2,4,4,5)
test = [(var02,val21),(or_symbol,[(var01,val11),(var01,val12)])]
print test
print ' '.join(recurse_solve(test, []))


print cvars