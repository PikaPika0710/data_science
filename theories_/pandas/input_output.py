import numpy as np
import pandas as pd
# read csv
# df = pd.read_csv('example')
# print(df)

# df.to_csv('example3',index=True)

# read excel

# df = pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet2')
# print(df)

# df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet2')


df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

print(df[0])