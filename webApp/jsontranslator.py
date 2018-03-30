import json

def conditionInput(incons):
	duration = {}
	cons = json.loads(incons)
	for x in cons['subs']:
		duration[(int(x['t']), x['id'], int(x['g']), int(x['n']))] = int(x['dur'])
	print duration