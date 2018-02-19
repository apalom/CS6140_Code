# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 22:57:53 2018

@author: Alex Palomino
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\Alex Palomino\Google Drive\Classes\18_Spring\CS6140 Data Mining\CS6140 Project\Data\CSV\DAYV2PUB.CSV', header=0)
df.head() # shows first 5 rows
df.tail() # shows last 5 rows
list(df) # shows all column headers
df['TRIPPURP'].describe()

print(df.shape)
