# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 22:57:53 2018

@author: Alex Palomino
"""

import pandas as pd
import timeit

start_time = timeit.default_timer()

df = pd.read_csv(r'C:\Users\Alex Palomino\Google Drive\Classes\18_Spring\CS6140 Data Mining\CS6140 Project\Data\CSV\DAYV2PUB.CSV', header=0)
colNames = list(df) # shows all column headers
first5rows = df.head() # shows first 5 rows
df.tail() # shows last 5 rows

df['TRIPPURP'].describe()

print('Dataframe Shape:', df.shape)

elapsed = timeit.default_timer() - start_time

# timeit statement
print('Execution time: {0:.4f} sec'.format(elapsed))

