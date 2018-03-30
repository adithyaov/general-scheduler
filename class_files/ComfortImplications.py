class ComfortImplications():
	"""docstring for ComfortImplications"""
	def __init__(self, arg):
		self.graph = {}
		self.graph['xtdp'] = {}
		self.graph['xtsgnd'] = {}
		self.graph['x!tsgndp'] = {}
		self.graph['xtd'] = {}
		self.graph['xtp'] = {}
		self.graph['xgdp'] = {}
		self.graph['xgd'] = {}
		self.graph['xgp'] = {}
		self.graph['lkgd'] = {}

def teacher_forbidden0(vector):
	if not vector:
	    for (t, d, p) in vector:
	        comfort_true_list.append(negation(('xtdp', (t, d, p))))

def teacher_forbidden1(vector):
	if not vector:
	    for (t, d) in vector:
	        comfort_true_list.append(negation(('xtd', (t, d))))


def teacher_forbidden2(vector):
	if not vector:
	    for (t, p) in vector:
	        comfort_true_list.append(negation(('xtp', (t, p))))


def teacher_requested0(vector):
	if not vector:
	    for (t, d, p) in vector:
	        comfort_true_list.append(('xtdp', (t, d, p)))


def teacher_requested1(vector):
	if not vector:
	    for (t, d) in vector:
	        comfort_true_list.append(('xtd', (t, d)))


def teacher_requested2(vector):
	if not vector:
	    for (t, p) in vector:
	        comfort_true_list.append(('xtp', (t, p)))


def group_forbidden0(vector):
	if not vector:
	    for (g, d, p) in vector:
	        comfort_true_list.append(negation(('xgdp', (g, d, p))))


def group_forbidden1(vector):
	if not vector:
	    for (g, d) in vector:
	        comfort_true_list.append(negation(('xgd', (g, d))))


def group_forbidden2(vector):
	if not vector:
	    for (g, p) in vector:
	        comfort_true_list.append(negation(('xgp', (g, p))))


def group_requested0(vector):
	if not vector:
	    for (g, d, p) in vector:
	        comfort_true_list.append(('xgdp', (g, d, p)))


def group_requested1(vector):
	if not vector:
	    for (g, d) in vector:
	        comfort_true_list.append(('xgd', (g, d)))


def group_requested2(vector):
	if not vector:
	    for (g, p) in vector:
	        comfort_true_list.append(('xgp', (g, p)))


# 2) Avoiding groups and teachers overlapping

def teacher_no_overlap(vector):
	if not vector:
	    for (t1, t2) in vector:
	        for d in days:
	            for p in periods[d]:
	                comfort_graph['xtdp'][(t1, d, p)].append(
	                    negation(('xtdp', (t2, d, p))))
	                comfort_graph['xtdp'][(t2, d, p)].append(
	                    negation(('xtdp', (t1, d, p))))

def group_no_overlap(vector):
	if not vector:
	    for (g1, g2) in vector:
	        for d in days:
	            for p in periods[d]:
	                comfort_graph['xgdp'][(g1, d, p)].append(
	                    negation(('xgdp', (g2, d, p))))
	                comfort_graph['xgdp'][(g2, d, p)].append(
	                    negation(('xgdp', (g1, d, p))))

# 3) Number of teaching days for a teacher

def teaching_days(vector):
	if not vector:
	    for (t, n) in vector:
	        atmost_var_list = []
	        atleast_var_list = []
	        for d in days:
	            atmost_var_list.append(('xtd', (t, d)))
	            atleast_var_list.append(negation(('xtd', (t, d))))

	        atmost_n = Cardinality(atmost_var_list, n)
	        comfort_true_list.append(atmost_n.form())

	        atleast_n = Cardinality(atleast_var_list, (no_of_days - n))
	        comfort_true_list.append(atleast_n.form())

# 4) Work day duration: ('xgdp' ∧ 'xgd(p+k−1)') => 'lkgd' min(periods(d)) <= p <= max(periods(d)) - k + 1
#                     ('lkgd' => (or, ('xgdp' ^ 'xgd(p+k-1)')) min(periods(d)) <= p  <= max(periods(d)) - k+1

#                     also for every working day: 'xgd' => 'lkgd'
#                     atmost n hours:  negation('lkgd') for all k > n

def work_day_duration(vector):
	if not vector:
	    for (g, k, d) in vector:
	        comfort_graph['lkgd'][(g, k, d)] = []

	        or_list = []
	        for p in range(min(periods[d]), max(periods[d]) - k + 2):
	            or_list.append(
	                ('and', [('xgdp', (g, d, p)), ('xgdp', (g, d, p + k - 1))]))
	            comfort_true_list.append(('or', [negation(('xgdp', (g, d, p))), negation(
	                ('xgdp', (g, d, p + k - 1))), ('lkgd', (k, g, d))]))

	        comfort_graph['lkgd'][(g, k, d)].append(('or', or_list))

# Atmost n hours on day d for group g

def duration_upper_limit(vector):
	if not vector:
	    for (g, d, n) in vector:
	        for k in range(n, max(periods[d]) + 1):
	            comfort_true_list.append(negation(('lkgd', (k, g, d))))

# Atleast n hours on day d for group g

def duration_lower_limit(vector):
	if not vector:
	    for (g, d, n) in vector:
	        comfort_graph['xgd'][(g, d)].append(
	            ('lkgd', (n, g, d)))  # Not convinced

# 5) Idle duration cardinality('xtgdp')

# Idle periods of length k not allowed

def teacher_max_idle_length(vector):
	if not vector:
	    for (t, k) in vector:
	        comfort_true_list.append(negation(('ikt', (k, t))))

# Atmost one idle period for a teacher per day

def teacher_atmost_one_idle_period(vector):
	if not vector:
	    for t in vector:
	        var_list = []
	        for d in days:
	            for p in range(min(periods[d]) + 1, max(periods[d] - 1) + 1):
	                var_list.append(('itdp', (t, d, p)))

	        comfort_true_list.append(single(var_list))

# Atmost k idle periods for a teacher in a week

def teacher_atmost_k_idle_period(vector):
	if not vector:
	    for (t, k) in vector:
	        var_list = []
	        for d in days:
	            for p in periods[d]:
	                var_list.append(('itdp', (t, d, p)))

	        atmost_k = Cardinality(var_list, k)
	        comfort_true_list.append(atmost_k.form())

# For groups
# Idle periods of length k not allowed

def group_max_idle_length(vector):
	if not vector:
	    for (g, k) in vector:
	        comfort_true_list.append(negation(('ikg', (k, g))))

# Atmost one idle period for a group per day

def group_atmost_one_idle_period(vector):
	if not vector:
	    for g in vector:
	        var_list = []
	        for d in days:
	            for p in range(min(periods[d]) + 1, max(periods[d] - 1) + 1):
	                var_list.append(('igdp', (g, d, p)))

	        comfort_true_list.append(single(var_list))

# Atmost k idle periods for a teacher in a week

def group_atmost_k_idle_period(vector):
	if not vector:
	    for (g, k) in vector:
	        var_list = []
	        for d in days:
	            for p in periods[d]:
	                var_list.append(('igdp', (g, d, p)))

	        atmost_k = Cardinality(var_list, k)
	        comfort_true_list.append(atmost_k.form())

# 6) Forbidden hours and requested hours:
# Favoured periods: 'xtsgnd' => 'x!tsgndp1' or ...

def favoured_hours(vector):
	if not vector:  # dict = {(t,s,g,n):[p]}
	    confort_graph['xtsgnd'] = defaultdict(lambda: [])
	    for (t, s, g, n) in vector.keys():
	        for d in days:
	            comfort_graph['xtsgnd'][(t, s, g, n, d)] = []
	            or_list = []
	            for p in vector[(t,s,g,n)]:
	                if bic3(d, p):
	                    or_list.append(('xtsgndp', (t, s, g, n, d, p)))
	    
	            comfort_graph['xtsgnd'][(t, s, g, n, d)].append(('or', or_list))

#first or last last lesson in a day: 'x!tsgndp' => (and, negation('xgdp')) or ('and', negation('xgdp'))

def last_first_hours(vector):
	if not vector:
	    for (t, s, g, n) in vector:
	        for d in days:
	            for p in periods[d]:
	                comfort_graph['x!tsgndp'][(t, s, g, n, d, p)] = []
	                and_list1 = []
	                for p2 in range(min(periods[d]), p + 1):
	                    and_list1.append(negation(('xgdp', (g, d, p2))))

	                and_list2 = []
	                for p2 in range(p + duration(t, s, g, n), max(periods[d] + 1)):
	                    and_list2.append(negation(('xgdp', (g, d, p))))

	                or_list = [('and', and_list1), ('and', and_list2)]
	    
	                comfort_graph['x!tsgndp'][(t, s, g, n, d, p)].append(('or', or_list))


# 7) lessons on non consecutive days:
#   'xtsgnd' => negation('xtsg(n + 1)(d+1))
#   except for last working day

def non_consecutive(self, vector):
	if not vector:
	    for (t, s, g, n) in vector:
	        for d in self.days[:-1]:
	            self.comfort_graph['xtsgnd'][(t, s, g, n, d)].append(negation(('xtsgnd', (t, s, g, n + 1, d + 1))))