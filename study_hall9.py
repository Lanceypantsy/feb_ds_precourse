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
