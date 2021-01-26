# # Imports
from sklearn.datasets import load_iris
# import numpy as np
from math import inf

# # Read in data set
# iris_dataset = load_iris()['data']

# # Find the average iris
# avg_iris = np.mean(iris_dataset, axis=(0, 1))

# print(avg_iris)

# def find_smallest_number(arr):
#     # your code here
#     smallest = inf

#     for obj in arr:
#         if type(obj) == float or type(obj) == int:
#             if obj < smallest:
#                 smallest = obj
#         else:
#             pass

#     return smallest

# ~(is float or is int) = (not float AND not int)

# import numpy as np
# import pandas as pd
# import random


# # Don't alter the code below
# random.seed(1)
# np.random.seed(1)
# cities = pd.Series([random.choice(['Denver', 'NYC', 'Chicago']) for _ in range(50)])
# temps = pd.Series(np.random.uniform(low=35, high=75, size=50))

# solution = temps.groupby(cities).mean()

data = load_iris()

print(len(data['data']), len(data['target']))

import numpy as np
from math import sqrt
gdp_05_19 = [3.5, 2.9, 1.9, -0.1, -2.5,
              2.6, 1.6, 2.2, 1.8, 2.5, 2.9,
              1.6, 2.4, 2.9, 2.3]
sp500_05_19 = [3, 13.62, 3.53, -38.49, 23.45,
                12.78, 0, 13.41, 29.6, 11.39,
                -0.73, 9.54, 19.42, -6.24, 28.8]
def cov_corr(rv_lst1, rv_lst2, pop=True):
    if pop:
        coeff = 1/(len(rv_lst1))
        ddof = 0
    else:
        coeff = 1/(len(rv_lst1)-1)
        ddof = 1

    rv_lst1_arr = np.array(rv_lst1)
    rv_lst2_arr = np.array(rv_lst2)

    cov = coeff * sum((rv_lst1_arr - np.mean(rv_lst1_arr))*(rv_lst2_arr - np.mean(rv_lst2_arr)))
    corr = cov/(np.std(rv_lst2_arr, ddof=ddof)*np.std(rv_lst1_arr, ddof=ddof))

    return  cov, corr
# Assign the covariance and correlation to the variables below
gdp_stock_cov, gpd_stock_corr = cov_corr(gdp_05_19, sp500_05_19, pop=True )