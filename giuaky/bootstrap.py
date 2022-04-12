# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.float_format', lambda x: '%.5f' % x) 

df = pd.read_csv('USvideos.csv');

featured_var = df['views']
print(featured_var);

Nboot = 500
def bootstrap(data, Nboot, statfun):
    data =  np.array(data)
    
    resampled_stat = []
    for k in range(Nboot):
        index = np.random.randint(0, len(data), len(data))
        sample = data[index]
        bstatistic = statfun(sample)
        resampled_stat.append(bstatistic)
        
    return resampled_stat
        
        
data_bootstrap = bootstrap(featured_var, Nboot, np.mean)

plt.hist(data_bootstrap,  bins=50)