import json

def conditionInput(incons):
	constraints_dict = {}
	duration = {}
	cons = json.loads(incons)
	for x in cons['subs']:
		duration[(int(x['t']), x['id'], int(x['g']), int(x['n']))] = int(x['dur'])
	
	constraints_dict['duration'] = duration

	constraints_dict['num_t'] = cons['no_t']

	constraints_dict['num_s'] = cons['no_s']
	constraints_dict['num_g'] = cons['no_g']
	constraints_dict['n_max'] = cons['maxNoClass']
	constraints_dict['p_max'] = cons['no_p']
	constraints_dict['d_max'] = cons['dow']

	comfid = {}
	comfid['0'] = 'teacher_forbidden0'
	comfid['1'] = 'teacher_forbidden1'
	comfid['2'] = 'teacher_forbidden2'

	comfid['3'] = 'teacher_requested0'
	comfid['4'] = 'teacher_requested1'
	comfid['5'] = 'teacher_requested2'

	comfid['6'] = 'group_forbidden0'
	comfid['7'] = 'group_forbidden1'
	comfid['8'] = 'group_forbidden2'

	comfid['9'] = 'group_requested0'
	comfid['10'] = 'group_requested1'
	comfid['11'] = 'group_requested2'

	comfid['12'] = 'teacher_no_overlap'
	comfid['13'] = 'group_no_overlap'
	comfid['14'] = 'teaching_days'
	comfid['15'] = 'work_day_duration'
	comfid['16'] = 'duration_upper_limit'
	comfid['17'] = 'duration_lower_limit'
	
	comfid['18'] = 'teacher_max_idle_length'
	comfid['19'] = 'teacher_atmost_one_idle_period'
	comfid['20'] = 'teacher_atmost_k_idle_period'
	
	comfid['21'] = 'group_max_idle_length'
	comfid['22'] = 'group_atmost_one_idle_period'
	comfid['23'] = 'group_atmost_k_idle_period'
	comfid['24'] = 'favoured_hours'
	comfid['25'] = 'last_first_hours'

	for x in comfid.keys():
		constraints_dict[comfid[x]] = []

	for x in cons['comfConst']:
		if(int(x['ctype']) == 1):
			if(int(x['p']) == 0):
				constraints_dict[comfid['1']].append((int(x['t']), int(x['d']) ))
			elif(int(x['d']) == 0):
				constraints_dict[comfid['2']].append((int(x['t']), int(x['p']) ))
			else:
				constraints_dict[comfid['0']].append((int(x['t']), int(x['d']), int(x['p']) ))
		elif(int(x['ctype']) == 2):
			if(int(x['p']) == 0):
				constraints_dict[comfid['4']].append((int(x['t']), int(x['d']) ))
			elif(int(x['d']) == 0):
				constraints_dict[comfid['5']].append((int(x['t']), int(x['p']) ))
			else:
				constraints_dict[comfid['3']].append((int(x['t']), int(x['d']), int(x['p']) ))
		elif(int(x['ctype']) == 3):
			if(int(x['p']) == 0):
				constraints_dict[comfid['7']].append((int(x['g']), int(x['d']) ))
			elif(int(x['d']) == 0):
				constraints_dict[comfid['8']].append((int(x['g']), int(x['p']) ))
			else:
				constraints_dict[comfid['6']].append((int(x['g']), int(x['d']), int(x['p']) ))

	print "conts:-"
	print constraints_dict