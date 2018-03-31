from StaticVariables import *


class NaiveRoomAlloc():
    """docstring for NaiveRoomAlloc"""
    def __init__(self):
        super(NaiveRoomAlloc, self).__init__()
        self.graph['x!tsgndpr'] = {}
        self.graph['x!tdpr'] = {}
        self.graph['xtsgndpr'] = {}
        self.graph['xtdpr'] = {}


    def form_variables():

        for (t, s, g, n, d, p) in self.graph['x!tsgndp'].keys():
            for r in StaticVariables.rooms:
                if ric1(t, s, g, n, r):
                    self.room_graph['x!tsgndpr'][(t, s, g, n, d, p, r)] = []
                    self.room_graph['xtsgndpr'][(t, s, g, n, d, p, r)] = []

        for (t, d, p) in self.graph['xtdp'].keys():
            for r in StaticVariables.rooms:
                self.room_graph['x!tdpr'][(t, d, p, r)] = []


    def basic_implications():
        for (t, s, g, n, d, p1, r) in self.graph['x!tsgndpr'].keys():
            for p2 in StaticVariables.periods[d]:
                if ric1(t, s, g, n, r) and bic1(t, s, g, n, d, p1, p2):
                    self.graph['x!tsgndpr'][(t, s, g, n, d, p1, r)].append(
                        ('xtsgndpr', (t, s, g, n, d, p2, r))
                    )

        for (t, s, g, n, d, p2, r) in self.graph['xtsgndpr'].keys():
            or_list = []
            for p1 in StaticVariables.periods[d]:
                if ric1(t, s, g, n, r) and bic2(t, s, g, n, d, p1, p2):
                    or_list.append(('x!tsgndpr', (t, s, g, n, d, p1, r)))
            self.graph['xtsgndpr'][(t, s, g, n, d, p2, r)].append(
                (StaticVariables.or_head, or_list)
            )

        for (t, s, g, n, d, p, r) in self.graph['x!tsgndpr'].keys():
            self.graph['x!tsgndpr'][(t, s, g, n, d, p, r)].append(
                ('x!tsgndp', (t, s, g, n, d, p))
            )

        for (t, s, g, n, d, p, r) in self.graph['xtsgndpr'].keys():
            self.graph['xtsgndpr'][(t, s, g, n, d, p, r)].append(
                ('xtsgndp', (t, s, g, n, d, p))
            )

        for (t, d, p, r) in self.graph['xtdpr'].keys():
            self.graph['xtdpr'][(t, d, p, r)].append(
                ('xtdp', (t, d, p))
            )


        multi_dict = {}
        for (t, s, g, n, d, p, r) in self.graph['x!tsgndpr'].keys():
            multi_dict[(t, s, g, n, d, p)] = []

        for (t, s, g, n, d, p, r) in self.graph['x!tsgndpr'].keys():
            multi_dict[(t, s, g, n, d, p)].append(('x!tsgndpr', (t, s, g, n, d, p, r)))

        for (t, s, g, n, d, p) in multi_dict.keys():
            self.graph['x!tsgndp'].append((or_head, multi_dict[(t, s, g, n, d, p)]))



        multi_dict = {}
        for (t, s, g, n, d, p, r) in self.graph['xtsgndpr'].keys():
            multi_dict[(t, s, g, n, d, p)] = []

        for (t, s, g, n, d, p, r) in self.graph['xtsgndpr'].keys():
            multi_dict[(t, s, g, n, d, p)].append(('xtsgndpr', (t, s, g, n, d, p, r)))

        for (t, s, g, n, d, p) in multi_dict.keys():
            self.graph['xtsgndp'].append((or_head, multi_dict[(t, s, g, n, d, p)]))



        multi_dict = {}
        for (t, d, p, r) in self.graph['xtdpr'].keys():
            multi_dict[(t, d, p)] = []

        for (t, d, p, r) in self.graph['xtdpr'].keys():
            multi_dict[(t, d, p)].append(('xtdpr', (t, d, p, r)))

        for (t, d, p) in multi_dict.keys():
            self.graph['xtdp'].append((or_head, multi_dict[(t, d, p)]))


    def correctness_implications():

        multi_dict = {}
        for (t, d, p, r) in self.graph['xtdpr'].keys():
            multi_dict[t] = []

        for (t, d, p, r) in self.graph['xtdpr'].keys():
            multi_dict[t].append(('xtdpr', (t, d, p, r)))

        for t in multi_dict.keys():
            self.true_list.append(single(multi_dict[t]))


        multi_dict = {}
        for (t, d, p, r) in self.graph['xtdpr'].keys():
            multi_dict[r] = []

        for (t, d, p, r) in self.graph['xtdpr'].keys():
            multi_dict[r].append(('xtdpr', (t, d, p, r)))

        for r in multi_dict.keys():
            self.true_list.append(single(multi_dict[r]))












