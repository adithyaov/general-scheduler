class Parser():
    """docstring for Parser"""

    def __init__(self, graph):
        self.graph = graph
    
    def compute_result(self, num_results=3):
        result_graphs = {}

        for i in graph:
            for j in graph[i]:
                bool_list.append(Implies(ParseVal((i, j)), ParseVal(graph[i][j])))

        bool_list.append(Implies(True, ParseVal(true_list)))

        for i in range(num_results):
            bool_result = compute_bool(bool_list)

            if bool_result[0] == False:
                break

            truth_assignments = bool_result[1]
            not_again = []

            for x in truth_assignments.decls():
                not_again.append(Bool(str(x)) != truth_assignments[x])

            result_graph = {}

            for x in truth_assignments:
                y = str(x)[2:-1].split('\', ')
                result_graph[y[0]] = {
                        True: [],
                        False: []
                        }

            for x in truth_assignments:
                y = str(x)[2:-1].split('\', ')
                result_graph[y[0]][bool(truth_assignments[x])].append(tuple(map(int, y[1][1:-1].split(','))))
            
            bool_list.append(Or(not_again))
            result_graphs[i] = result_graph

        return result_graphs


