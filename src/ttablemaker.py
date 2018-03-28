from parser import *
from tabulate import tabulate

scheduled = result_graph['xtsgndp'][True]

ttable = [[ [] for i in range(len(periods)) ] for i in range(len(days))]

for (t, s, g, n, d, p) in scheduled:
    ttable[d][p].append((t, s, g, n))

for i in range(len(ttable)):
    ttable[i].insert(0, "Day {}".format(str(i)))

print tabulate(ttable, headers=["X"]+max(periods), tablefmt='fancy_grid').encode('utf-8')