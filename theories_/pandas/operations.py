import pandas as pd
def times2(x):
    return x*2;

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df)
print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())

print(df['col2'].apply(times2))
print(df['col3'].apply(len))
print(df['col1'].sum())



del df['col1']
print(df)
print(df.columns)
print(df.index)
print(df.sort_values(by='col2'))
print(df.isnull())



data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))
