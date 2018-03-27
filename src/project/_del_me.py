#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 23:02:36 2018

@author: nan
"""
import numpy as np

def bic1(t, s, g, n, d, p1, p2):
    truth = [
        (p1 >= np.min(range(5))),
        (p1 <= np.max(range(5)) - 1),
        (p2 >= p1),
        (p2 <= p1 + 1)
    ]
    print truth
    return np.prod(truth)

print bic1(0, 0, 0, 0, 0, 0, 0)