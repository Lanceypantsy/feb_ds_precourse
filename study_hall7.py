from sklearn.datasets import load_iris
import pandas as pd
# import matplotlib.pyplot as plt
# from math import sqrt
# from scipy.stats import t
# from scipy.stats import norm
import numpy as np
# import card

# this = card.Card('hearts', 9)

# print(this)

# class Deck():
#     def __init__(self, shuffled=False):
#         self.stack = []
#         self.shuffled = shuffled

#         suits = ['spades', 'clubs', 'hearts', 'diamonds']
#         ranks = range(1,14)

#         for rank in ranks:
#             for suit in suits:
#                 self.stack.append(card.Card(suit, rank))

# my_deck = Deck()
# print(my_deck.stack[-5:])

data = pd.DataFrame(load_iris()['data'])
data.columns = ['sepal_l', 'sepal_w', 'petal_l', 'petal_w']
# num_bins = 20
# col_name = 'sepal_l'

# y = data.hist(col_name, bins=num_bins)
# x = data.plot(y=col_name, bins=num_bins, kind='hist')

# print(x)
# print(y)

# n = 18
# mu_0 = 72
# x_bar = 68
# s = 10

# t_stat = (x_bar - mu_0) / (s / sqrt(n))

# print(t.cdf(x=t_stat, df=n-1))
# print(norm.cdf(x=68, loc=72, scale=(s/sqrt(n))))

# gdp_05_19 = [3.5, 2.9, 1.9, -0.1, -2.5,
#              2.6, 1.6, 2.2, 1.8, 2.5, 2.9,
#              1.6, 2.4, 2.9, 2.3]

# sp500_05_19 = [3, 13.62, 3.53, -38.49, 23.45,
#                12.78, 0, 13.41, 29.6, 11.39,
#                -0.73, 9.54, 19.42, -6.24, 28.8]

# def cov_corr(data1, data2, pop=True):
#     if pop:
#         coeff = 1 / (len(data1))
#         ddof = 0
#     else:
#         coeff = 1 / (len(data1) - 1)
#         ddof = 1

#     x_sum = sum([(x - np.mean(data1))**2 for x in data1])
#     y_sum = sum([(y - np.mean(data1))**2 for y in data2])
#     denom = np.sqrt(x_sum * y_sum)

#     cov = coeff * sum([(x - np.mean(x))*(y - np.mean(y)) for x, y in zip(data1, data2)])
#     corr = cov / (np.std(data1, ddof=ddof) * np.std(data2, ddof = ddof))

#     return cov, corr

# arr = np.arange(0, 300, 3)

# arr[arr % 2 == 0] = 2

# print(arr)

# print(data[data[:,0] > 5])
# print(data)

# By convention pandas is imported as below:
# import pandas as pd

# # Create a series
# prices = pd.Series([1,1,2,3,5],
#                    index=[12, 13, 14, 15, 0])

# data.index = [f'flower #{count}' for count in range(150)]

# print(data.iloc[['flower #1', 'flower #2'], 'sepal_l'])
