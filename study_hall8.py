import numpy as np

# A = np.arange(9).reshape(3, 3)
# x = np.ones((1, 3))

# print(A.dot(x))

# lst = [1, 2, 3, 4, 5, 6]

# print(lst[lst > 3])

# lst = [0.1, 0.2, 0.25, 0.35]

# prod = 1

# for prob in lst:
#     prod *= prob

# print(prod)

# from scipy.stats import norm

# data = np.array([ 12.1085187 ,  12.10867427,  11.21137858,  10.01311363,
#                   10.79744224,  13.19280269,  12.44086123,  11.88810057,
#                   10.70064104,  11.50382741])

# data_mean = sum(data) / len(data)
# data_sigma_sq = np.std(data)**2

# mus = [10, 11, 12, data_mean]
# sigmas = [1.0, 1.1, 1.2, data_sigma_sq]

# def log_likelihood_normal_two_parameters(mu, sigma_sq, data_in):
#     """
#     Consume the parameters mu (mean) and sigma_sq (variance) of a normal
#     distribution, and compute the likelihood of a fixed dataset (data_in).
#     """
#     normal = norm(mu, np.sqrt(sigma_sq))
#     likelihoods = [normal.pdf(datum) for datum in data_in]
#     return np.sum(np.log(likelihoods))

# def minus_log_likelihood_normal_two_parameters(mu, sigma, data_in):
#     return - log_likelihood_normal_two_parameters(mu, sigma, data_in)

# from itertools import product

# for mu, sigma_sq in product(mus, sigmas):
#     print("Log-Lik of Two Parameter Normal Model With mu={0}, sigma_sq={1}: {2:3.2f}".format(
#         mu, sigma_sq, log_likelihood_normal_two_parameters(mu, sigma_sq, data)))

# Log-Lik of Two Parameter Normal Model With mu=-1, sigma_sq=0.5: -102.05
# Log-Lik of Two Parameter Normal Model With mu=-1, sigma_sq=1: -82.66
# Log-Lik of Two Parameter Normal Model With mu=-1, sigma_sq=2: -81.63
# Log-Lik of Two Parameter Normal Model With mu=0, sigma_sq=0.5: -52.85
# Log-Lik of Two Parameter Normal Model With mu=0, sigma_sq=1: -58.06
# Log-Lik of Two Parameter Normal Model With mu=0, sigma_sq=2: -69.33
# Log-Lik of Two Parameter Normal Model With mu=1, sigma_sq=0.5: -103.64
# Log-Lik of Two Parameter Normal Model With mu=1, sigma_sq=1: -83.46
# Log-Lik of Two Parameter Normal Model With mu=1, sigma_sq=2: -82.03


# # Imports
# import numpy as np
# from sklearn.datasets import load_iris

# # Your code below
# iris_data = load_iris()['data']

# vol_column_vec = (np.pi * iris_data[:, 2] * (iris_data[:, 0]**2)/3).reshape(-1,1)

# iris_w_vol = np.concatenate((iris_data, vol_column_vec ), axis=1)

# print(iris_w_vol[:5])

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# # df = pd.read_csv('../../Data/students.csv')

from sklearn.datasets import load_iris

# df = pd.DataFrame(load_iris()['data'])

# df.columns = ['sep_w', 'sep_l', 'pet_w', 'pet_l']

# df.plot(y = 'sep_w', kind='hist', bins=10)
# plt.show()

# import scipy.stats as stats

# sd = 2.75
# mean_sd = 2.75 / np.sqrt(50)

# print(stats.t.interval(alpha=.95, df=49, loc=39.9, scale=mean_sd))

prices = pd.Series([1,1,2,3,5],
                   index=['apple', 'pear', 'banana', 'mango', 'jackfruit'])

inventory = pd.Series([10, 50, 41, 22],
                      index=['pear', 'banana', 'mango', 'apple'])

discount_prices = prices * .9

produce = pd.DataFrame({'price': prices,
                                'inventory': inventory,
                                'discount_price': discount_prices})

# print(produce)

data = load_iris()['data']
df = pd.DataFrame(data)

df.index = [f'flower #{num}' for num in range(1, 151)]

produce.drop(['price', 'inventory'], axis = 1, inplace=True)

print(produce)
