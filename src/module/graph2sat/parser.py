from graph import *

nvars = [len(graph[i]) for i in graph]
cvars = [[(i,j) for j in (graph[i])] for i in graph]

print cvars
print nvars
