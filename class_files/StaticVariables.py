import numpy as np

class StaticVariables():
    """docstring for StaticVariables"""
    or_head = 'or'
    and_head = 'and'
    p_max = 7

    num_t = 8
    num_s = 4
    num_g = 5
    teachers = np.array(range(num_t))
    subjects = np.array(range(num_s))
    groups = np.array(range(num_g)) 

    duration = {
        (0, 0, 0, 1): 3,
        (0, 0, 1, 2): 3,
        (0, 0, 2, 3): 3
    }