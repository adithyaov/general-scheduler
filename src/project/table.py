from parser import *
from tabulate import tabulate

xt = truth_dict2['xtsgndp']
tt = [[ [] for i in range(len(periods)) ] for i in range(len(days))]

for x in xt:
    cl = map(int, x.replace('(','').replace(')','').split(','))
    tt[cl[4]][cl[5]].append(cl)
    
print tabulate(tt)