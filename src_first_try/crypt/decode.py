'''
Objective: Give an encoded name, returns the set of key value pairs
'''

from encode import encode

def decode(variable, inter_seperator='.', intra_seprator='_'):
	'''
	This function decodes a given encoded variable
	'''
	var_components = [x.split(intra_seprator) for x in variable.split(inter_seperator)]
	component_dict = {}
	for c in var_components:
		if len(c) == 2:
			component_dict[c[0]] = c[1]
	return component_dict


def test_decode():
	'''
	Simple assertions to check the correctness of decode
	'''
	temp = {
		't': 'valsa',
		's': 'sem5'
	}
	assert(decode(encode(t='valsa', s='sem5')) == temp)

test_decode()