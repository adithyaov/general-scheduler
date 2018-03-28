from parser import *
from tabulate import tabulate

#c = 0
#
#for x in bool_graph:
#    a = len(bool_graph[x])
#    if a == 0:
#        c += 1
        
#print truth_dict2['x!tsgndp']
#print truth_dict2['xtsgndp']
#
#
#print 'Total: ', len(result)
#print 'xtsgndp: ',len(truth_dict2['xtsgndp'])
#print 'x!tsgndp: ', len(truth_dict2['x!tsgndp'])

scheduled = truth_dict2['xtsgndp']

ttable = [[ [] for i in range(len(periods)) ] for i in range(len(days))]

for x in scheduled:
    cl = map(int, x.replace('(','').replace(')','').split(','))
    ttable[cl[4]][cl[5]].append(cl)

for i in range(len(ttable)):
    ttable[i].insert(0, "Day" + str(i))

print tabulate(ttable,headers=["X"]+periods[0], tablefmt='fancy_grid')

