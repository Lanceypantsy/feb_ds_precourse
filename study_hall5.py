from sklearn.datasets import load_iris
import numpy as np

iris_data = load_iris()['data']


# col1 = iris_data[:,0]
# col2 = iris_data[:,1]
# col3 = iris_data[:,2]
# col4 = iris_data[:,3]

# col1 = np.round((col1 - min(col1)) / (max(col1) - min(col1)), 2)
# col2 = np.round((col2 - min(col2)) / (max(col2) - min(col2)), 2)
# col3 = np.round((col3 - min(col3)) / (max(col3) - min(col3)), 2)
# col4 = np.round((col4 - min(col4)) / (max(col4) - min(col4)), 2)

# matrix = np.array([col1, col2, col3, col4]).transpose()

# print(matrix)

# min_ = np.min(iris_data, axis=0)
# max_ = np.max(iris_data, axis=0)
# ptp = np.ptp(iris_data, axis=0)

# print(ptp)

# iris_data_normalized = np.round((iris_data - min_) / (max_ - min_), 2)

# print(iris_data_normalized)

# vec = np.array([1, 2, 3, 4])

# print(vec.reshape(-1,1).shape)

# A = np.array([[1,7], [3,6]])
# B = np.array([[3, 1], [-8, 8]])

# print(A.dot(A.transpose()))

# import numpy as np

# matrix_A = np.array([[3, 5], [1, 7]])
# matrix_B = np.array([[2, 11],[1, 4]])

# A_times_B = np.dot(matrix_A, matrix_B)
# B_times_A = np.dot(matrix_B, matrix_A)

# print(f'AB =\n {A_times_B}\n')
# print(f'BA =\n {B_times_A}')

# a = np.array([1, 2, 3, 4, 5]).dot(np.array([5, 4, 3, 2, 1]))
# print(a)


# def matmul(mat1, mat2):
#     pass

# matrix_A = np.array([[3, 5], [1, 7]])
# i_2 = np.array([[1, 0],[0, 1]])


# print(i_2.dot(matrix_A))

# num = 12
# num_i = 1 / 12

# print(num * num_i)

# b = (X'X)-1X'y

# A = np.array([[-1, -7],[3, 3]])
# A_inv = np.linalg.inv(A)

# b = np.array([[-53],[33]])

# print(A_inv.dot(b))

iris_data[1]