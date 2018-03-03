'''
Objective: Give a unique var_name to a set of inputs
'''

def encode(var_def='x', **kwargs):
	'''
	This function encodes a given arguments into a proper variable
	'''
	encoded_var = var_def
	key_list = kwargs.keys()
	key_list.sort()
	for x in key_list:
		encoded_var = encoded_var + '.' + str(x) + '_' + str(kwargs[x])
	return encoded_var


def test_encode():
	'''
	Simple assertions to check the correctness of encode
	'''
	assert(encode(t='valsa', s='sem5') == 'x.s_sem5.t_valsa')
	assert(encode(var_def='y!', t='valsa', s='sem5') == 'y!.s_sem5.t_valsa')
