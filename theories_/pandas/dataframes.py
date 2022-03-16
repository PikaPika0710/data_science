import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns ='W X Y Z'.split())

print(df)

print(df['W'])
print(df[['W','Z']])

df['new'] = df['W'] + df['Y']
print(df)
# drop a column
df.drop('new', axis=1, inplace=True)
print(df)
# drop a row
# df.drop('A', axis=0, inplace=True)
# print(df)
# selecting a row
print(df.loc['B'])
print(df.iloc[1])
# selecting a subset rows and column
print(df.loc['B','Y'])
print(df.loc[['A','B'],['W','Y']])


#condition selection
print(df)
print(df > 0)
print(df[df>0])
print(df[df['W']>0])
print(df[df['W']>0]['Y'])
print(df[df['W']>0][['Y','X']])
print(df[(df['W']>0) & (df['Y'] > 0)])

#index details
print(df.reset_index())


df['States'] = 'CA NY WY OR CO'.split()
print(df)
df.set_index('States', inplace=True)
print(df)


# multi-index and index hierarchy
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df)
print(df['A'])
print(df.loc['G1'])
print(df.loc['G1'].loc[1])
df.index.names = ['Group', 'Num']
print(df)
print(df.xs('G1'))
print(df.xs(['G1',1]))
print(df.xs(1, level='Num'))