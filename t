#!/usr/local/bin/python3

import pandas as pd
import re

#zero padding
#i = 136
#z = 10

#print(f'{i:0{z}}')


wb = pd.ExcelFile('slate.xlsx')
ws = wb.sheet_names[0]
df = wb.parse(ws, header=None)

#print(df)
#print(df.axes)
#print(df.values[-1])
#print(df.shape)
#print(df.size)
#print(df.describe(include='all'))
#print(df.loc[:2])
#print(df.iloc[84:])
#print(df.head(5))

#(rows, cols) = df.shape
#print(df.info())
#print(df.to_string())

# get rid of empty cells
df.dropna(inplace = True)
cols = [
    'agency',
    'client',
    'product',
    'title',
    'isci',
    'duration',
    'audio',
    'date',
    'format'
]

df.columns = cols


import datetime
slate_info = {}
for index,row in df.iterrows():
    print('')
    if re.match(r'duration', row['duration'], re.IGNORECASE):
        continue

    slate_filename = row['title']
    slate_info[row['title']] = []

    for i in cols:
        value = row[i]
        if isinstance(value, datetime.datetime):
            value = value.strftime('%m/%d/%Y')

        print('\t{} -> {}'.format(i, value))


