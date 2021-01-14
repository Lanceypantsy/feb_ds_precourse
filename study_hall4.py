import numpy as np

# arr = np.array([np.arange(1, 63, 3)])

# states = {1: 'Colorado', 2: 'Wyoming', 3: 'New Mexico'}

# states_codified = np.array([1, 2, 1, 1, 1, 3, 1, 2, 3, 1, 1])
# temps = np.array([np.random.random()*70 for _ in range(11)])

# print(temps[states_codified == 1])

arr = np.array([np.random.randint(3, 10, 8)])

# new_arr = []

# for ele in arr:
#     new_arr.append(ele + 10)

# new_arr = arr * 10 - 10

# print(arr)
# print(new_arr)

from sklearn.datasets import load_iris

# np.set_printoptions(suppress=True)

data = load_iris()['data']

# avg_iris = data.mean(axis=0)

# print(data.shape)

# data_minus_mean = data - avg_iris

# print(data_minus_mean)
# # print(load_iris()['DESCR'])

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# arr2 = np.array([np.random.random()*10 for _ in range(7)])

# print(arr)
# print(arr2)

# print(arr + arr2)

# from sklearn.datasets import load_iris
# import numpy as np

# iris_data = load_iris()['data']

# # Your code below
# range_data = iris_data.ptp(axis = 0)
# min_data = iris_data.min(axis = 0)

# iris_data_normalized = np.round((iris_data - min_data) / range_data, 2)

# print(iris_data_normalized)

print(load_iris()['DESCR'])
