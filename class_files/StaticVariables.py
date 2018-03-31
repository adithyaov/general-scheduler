import numpy as np

class StaticVariables():
    """docstring for StaticVariables"""
    or_head = 'or'
    and_head = 'and'
    not_head = 'not'
    p_max = 8
    days = range(6)
    num_t = 8
    num_s = 4
    num_g = 5
    periods = [np.array(range(p_max)) for _ in range(len(days))]
    teachers = np.array(range(num_t))
    subjects = np.array(range(num_s))
    groups = np.array(range(num_g)) 

    duration = {
        (0, 0, 0, 1): 3,
        (1, 2, 1, 2): 3,
        (3, 0, 2, 3): 3,
        (2, 3, 0, 1): 3,
        (0, 0, 1, 2): 3,
        (3, 1, 2, 3): 3,
    }
    
    tdata = {
        "may" : [0, 1],
        "june" : [1, 2],
        "july" : [3]
    }
    
    sdata = {
        0: [0, 3],
        1: [3],
        2: [3, 0],
        3: [2, 1],
    }