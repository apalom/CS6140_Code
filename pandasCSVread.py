# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 22:57:53 2018

@author: Alex Palomino
"""

import pandas as pd
import timeit

start_time = timeit.default_timer()

whyIDdict = {}

df0 = pd.read_csv(r'C:\Users\Alex Palomino\Google Drive\Classes\18_Spring\CS6140 Data Mining\CS6140 Project\Data\CSV\DAYV2PUB.CSV', header=0)

df1 = df0.filter(['TDCASEID','TRAVDAY','STRTTIME','DWELTIME','ENDTIME','TRIPPURP',
                  'WHYFROM','WHYTO','WHYTRP1S','WHYTRP90','WHODROVE',
                  'CENSUS_D','CENSUS_R','DRIVER','AWAYHOME','FRSTHM','TDTRPNUM',
                  'TDWKND','TRPACCMP','TRPHHACC','TRVLCMIN','TRVL_MIN','TRWAITTM',
                  'VEHTYPE','VEHYEAR','VMT_MILE','HHFAMINC','HHSIZE','HHSTATE','HOMEOWN',
                  'NUMADLT','NUMONTRIP','PRMACT','PAYPROF','PROXY','PRMACT','R_AGE','R_SEX'], axis=1)

# build out DF table
colNames0 = list(df0) # shows all column headers
colNames1 = list(df1) # shows all column headers
first5rows0 = df0.head() # shows first 5 rows
first5rows1 = df1.head() # shows first 5 rows
last5rows0 = df0.tail() # shows last 5 rows
last5rows1 = df1.tail() # shows last 5 rows

df2 = pd.DataFrame(columns=colNames1)

# function call
from funcWhyID import funcWhyID
[df1, whyIDdict] = funcWhyID(df1, whyIDdict)

df0['TRIPPURP'].describe()

print('Dataframe Raw Shape:', df0.shape)
print('Dataframe Filtered Shape:', df1.shape)

elapsed = timeit.default_timer() - start_time

# timeit statement
print('Execution time: {0:.4f} sec'.format(elapsed))

