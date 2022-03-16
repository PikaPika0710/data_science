import pandas as pd

sal = pd.read_csv('Salaries.csv')

# def getAverageBasePay(year):
#     return sal[sal['Year'] == year]['BasePay'].mean()

print(sal.head)
print(sal.info())
print(sal['BasePay'].mean())
print(sal['OvertimePay'].max())
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
print(sal[sal['TotalPay'] == sal['TotalPay'].max()])
print(sal[sal['TotalPay'] == sal['TotalPay'].min()])

#df = pd.Series([getAverageBasePay(2011),getAverageBasePay(2012),getAverageBasePay(2013),getAverageBasePay(2014)], index = '2011 2012 2013 2014'.split())

print(sal.groupby('Year').mean()['BasePay'])
print(sal['JobTitle'].nunique())
print(sal.groupby('JobTitle').count().sort_values(by='Id', ascending=False)['Id'][:5])

b = sal[sal['Year']==2013].groupby('JobTitle').count()
c = sum(b['Id'] == 1)
print(c)

def find_chief(job_title):    
    if 'chief' in job_title.lower().split():
        return True
    else:
        return False

print(sum(sal['JobTitle'].apply(find_chief)))


sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['title_len', 'TotalPayBenefits']].corr())