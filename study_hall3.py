## Pandas Slicing

import numpy as np
import pandas as pd

# prices = pd.Series([1,1,2,3,5],
#               index=['apple', 'pear', 'banana', 'mango', 'jackfruit'])

# inventory = pd.Series([10, 50, 41, 22],
#               index=['pear', 'banana', 'mango', 'apple'])

# discount_prices = prices.apply(lambda x: .9*x if x>3 else x)

# produce = pd.DataFrame({'price':prices,
#                         'discount_price':discount_prices,
#                         'inventory':inventory})

# one_select = produce.loc[['pear', 'jackfruit']]

# produce['clearance_price'] = prices * .5

# two_clearance = produce.iloc[3]

# not_prices = pd.Series([1,1,2,3,5],
#               index=['apple', 'pear', 'banana', 'mango', 'jackfruit'])

# inventory = pd.Series([10, 50, 41, 22],
#               index=['pear', 'banana', 'mango', 'apple'])

my_arr = np.array((1, 2, 3)).reshape(-1, 1)

# my_2d_array = np.array([[[1, 2, 3],
#                          [4, 5, 6],
#                          [7, 8, 9]],
#                         [[9, 8, 7],
#                          [6, 5, 4],
                        #  [3, 2, 1]]])


# my_2d_array[:, 1, :] = 4

# print(my_2d_array)

new_arr = np.array([round(np.random.random()) for _ in range(24)]).reshape(6,4)
nums = np.array([np.random.choice([1, 2]) for _ in range(24)]).reshape(6,4)

print(new_arr)
print(nums)
print(new_arr[nums == 2])
