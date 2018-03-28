from parser import *

c = 0

for x in bool_graph:
    a = len(bool_graph[x])
    if a == 0:
        c += 1
        
print 'Total: ', len(result)
print 'x!tsgndp: ', len(truth_dict2['x!tsgndp'])
print 'xtsgndp: ', len(truth_dict2['xtsgndp'])

print 'x!tsgndp: ', truth_dict2['x!tsgndp']

print 'xtsgndp: ', truth_dict2['xtsgndp']