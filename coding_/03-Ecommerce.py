import pandas as pd


ecom = pd.DataFrame(pd.read_csv('Ecommerce-Purchases'))

# print(ecom)
# print(ecom.head())

# print(ecom.info())
# print(ecom['Purchase Price'].mean())
# print(ecom['Purchase Price'].min())
# print(ecom['Purchase Price'].max())
# print(ecom[ecom['Language'] == 'en'].count())
# print(ec
# 
# om[ecom['Job'] == 'Lawyer'].info())

# print(ecom.value_counts('AM or PM'))

# a = ecom.groupby('Job').count()
# b = a.sort_values(by='Address', ascending=False)
# print(b['Address'][:5])

# print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])
# print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])

# a = ecom[ecom['CC Provider'] == 'American Express']
# b = a[a['Purchase Price'] > 95].count()
# print(b)
# def isExprire(x):
#     if '25' in x.split('/'):
#             return True
#     return False
    
    
# print(sum(ecom['CC Exp Date'].apply(isExprire)))


def getProvider(x):
    return x[x.index('@')+1:]



# groupby('Email').count()
print(ecom['Email'].apply(getProvider).value_counts()[:5])