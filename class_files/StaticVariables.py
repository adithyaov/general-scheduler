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
        (0, 0, 1, 2): 3,
        (0, 0, 2, 3): 3
    }

    rooms = range(7)

    '''
    (t, s, g, n) = [room_set]
    '''

    # room_dict = {
    #     (t, s, g, n): [1, 2, 3]
    # }

