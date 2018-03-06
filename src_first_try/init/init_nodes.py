'''
Initialize all nodes in the graph
'''

from graph_format import graph_protocol, normalize_list, init_periods
from ...crypt.encode import encode

def graph_init(prev_graph, lessons, days, periods):
	'''
	lessons = [
		{
			't': 't1',
			's': 's1',
			'g': 'g1',
			'n': 1
		}
	]
	'''