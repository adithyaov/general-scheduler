from var import *

def bic0(t, s, g, n):
	truth = [
		(duration[(t, s, g, n)] > 0)
	]
	return np.prod(truth)

def bic1(t, s, g, n, d, p1, p2):
	truth = [
		(p1 > np.min(periods[d])),
		(p1 <= np.max(periods[d]) - duration[(t, s, g, n)] + 1),
		(p2 >= p1),
		(p2 <= p1 + duration[(t, s, g, n)] - 1)
	]
	return np.prod(truth)


def bic2(t, s, g, n, d, p1, p2):
	truth = [
		(p1 <= p2),
		(p1 >= p2 - duration[(t, s, g, n)] + 1),
		(p1 >= np.min(periods[d])),
		(p1 <= np.max(periods[d]) - duration[(t, s, g, n)] + 1)
	]
	return np.prod(truth)

def bic3(d, p):
	truth = [
		(p <= np.max(periods[d])),
		(p >= np.min(periods[d]))
	]
	return np.prod(truth)

def bic4(d, p):
	truth = [
		(p in periods[d])
	]
	return np.prod(truth)

def bic5(t, s, g, n, d, p):
	truth = [
		(p1 >= np.min(periods[d])),
		(p1 <= np.max(periods[d]) - duration[(t, s, g, n)] + 1)
	]
	return np.prod(truth)

def bic6(t, s, g, n):
	# this means tsgn belongs to lessons[t] and to lessons[g]
	truth = [
		(duration[(t, s, g, n)] > 0)
	]
	return np.prod(truth)


def bic7(d):
	truth = [
		(d in days)
	]
	return np.prod(truth)


def bic8(k, d, p):
	truth = [
		(k >= 1),
		(k <= len(periods[d]) - 2),
		(p >= np.min(periods[d]) + 1),
		(p <= np.max(periods[d]) - k)
	]
	return np.prod(truth)


def bic9(k, d):
	truth = [
		(k >= 1),
		(k <= len(periods[d]) - 2)
	]
	return np.prod(truth)

def bic10(k, d, p):
	truth = [
		(p >= np.min(periods[d]) + 1),
		(p <= np.max(periods[d]) - k)
	]
	return np.prod(truth)

def bic11(d, p):
	truth = [
		(p >= np.min(periods[d]) + 1),
		(p <= np.max(periods[d]) - 1)
	]
	return np.prod(truth)

def bic12(k, d, p):
	truth = [
		(k >= 1),
		(k <= np.max(periods[d]) - p)
	]
	return np.prod(truth)