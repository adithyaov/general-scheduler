from graph import *

nvars = [len(graph[i]) for i in graph]
cvars = [[(i,j) for j in (graph[i])] for i in graph]

print cvars
print nvars

def form_var(tup):
	var = ''
	for i in len(tup):
		var += str(tup[i])
	return var

def recurse_solve(formula, init_list):
	new_list = init_list
	if type(formula) == type([]):
		formula = ('and', formula)
	for x in formula[1]:
		if x[0] in ['and', 'or']:
			new_list.append('(')
			new_list.append(recurse_criteria(x, []))
			new_list.append(')')
		else:
			var = form_var(x)
			new_list.append(var)
		new_list.append(formula[0])
	return new_list[:-1]