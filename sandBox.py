# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:45:02 2018

@author: Alex Palomino
"""

import timeit

timeExec= []
start_time = timeit.default_timer()

elapsed = timeit.default_timer() - start_time
timeExec.append(elapsed)

print('Execution time: {0:.2f} sec'.format(elapsed))