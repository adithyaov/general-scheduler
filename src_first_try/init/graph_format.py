'''
This file with contain only the structure of the graph
'''

graph_protocol = {
	'graph_storage': 'dictionary',
	'duration_storage': 'dictionary',
	'negation_constant': '~'
}

def normalize_list(l):
	new_list = []
	for x in l:
		new_list.append(str(x).lower())
	return new_list	


def init_days(list_of_days=['mon', 'tue', 'wed', 'thu', 'fri']):
	return normalize_list(init_days)

def init_periods(num_period_list=[7]*5):
	main_list = []
	num_days = len(num_period_list)
	for i in num_period_list:
		main_list.append([1 + k for k in range(i)])
	return main_list

def init_teachers(list_of_teachers=['t1', 't2', 't3', 't4']):
	return normalize_list(list_of_teachers)

def init_groups(list_of_groups=['g1', 'g2', 'g3', 'g4']):
	return normalize_list(list_of_groups)