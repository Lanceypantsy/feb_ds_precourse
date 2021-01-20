import numpy as np
# from math import sqrt

# gdp_05_19 = [3.5, 2.9, 1.9, -0.1, -2.5,
#              2.6, 1.6, 2.2, 1.8, 2.5, 2.9,
#              1.6, 2.4, 2.9, 2.3]

# sp500_05_19 = [3, 13.62, 3.53, -38.49, 23.45,
#                12.78, 0, 13.41, 29.6, 11.39,
#                -0.73, 9.54, 19.42, -6.24, 28.8]


# def cov_corr(data1, data2, pop=True):
#     '''
#     This function takes in two lists of the same length representing random
#     variables. The function finds both the covariance and the correlation
#     between the two random variables and returns them in a tuple. You can
#     assume the lists given will always be the same length, and the data
#     will share some commonality.

#     Parameters
#     ----------
#     rv_lst1 : list-like object
#            A list or list-like object full of data representing a RV

#     rv_lst2 : list-like object
#            A list or list-like object full of data representin a RV

#     pop : bool
#             Default = True

#     Returns
#     -------
#     cov : float
#         A float representing the covariance between the two lists of data
#     corr : float
#         A float representing the correlation between the two lists of data
#     '''
#     if pop:
#         coeff = 1 / len(data1)
#         ddof = 0
#     else:
#         coeff = 1 / (len(data1) - 1)
#         ddof = 1

#     data1_arr = np.array(data1)
#     data2_arr = np.array(data2)

#     cov = coeff * sum((data1_arr - np.mean(data1_arr)) * (data2_arr - np.mean(data2_arr)))
#     corr = cov / (np.std(data1_arr, ddof=ddof) * np.std(data2_arr, ddof = ddof))

#     return cov, corr

# data1_arr = np.array(gdp_05_19)
# data2_arr = np.array(sp500_05_19)

# print(sum((data1_arr - np.mean(data1_arr)) * (data2_arr - np.mean(data2_arr))))

# import scipy.stats as stats

# print(stats.norm.cdf(59, loc=63, scale=2))

from math import pi

print(np.arcsin((np.sqrt(3)/2)) == pi/3)
