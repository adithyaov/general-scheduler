from parser import *
import numpy as np

#print 'Total: ', len(result)
print 'x!tsgndp: ', len(result_graph['x!tsgndp'][True]), len(duration)
print 'xtsgndp: ', len(result_graph['xtsgndp'][True]), np.sum([x for x in duration.values()])

#
#print 'x!tsgndp: ', truth_dict2['x!tsgndp']
#
#print 'xtsgndp: ', truth_dict2['xtsgndp']