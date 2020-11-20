import pandas as pd
import numpy as np

x = np.arange(10, dtype=int)
a = np.arange(10, 20, 1, dtype=int)
la = np.arange(20, 30, 1, dtype=int)
my_numpy_array = np.array([x, a, la]).T

my_dataframe = pd.DataFrame(my_numpy_array, columns=["first_column", "second_column", "third_column"])
my_dataframe.head(10)
my_dataframe.iloc[0, 0] = 997
my_dataframe.iloc[9, 1] = 998
my_dataframe.iloc[4, 0] = 1000
my_dataframe.iloc[1, 2] = 999
new_Data_frame = my_dataframe.iloc[3:7, 0:3]
new_Data_frame.iloc[0, 0] = -997
# print(new_Data_frame)
my_dataframe = my_dataframe.iloc[3:7, 1:3]
e = 100
for chislo in range(0,3):
    # my_dataframe.iloc[0:3, 1] = e
    my_dataframe.iloc[chislo, 1] = e
    e = e + 1


# my_dataframe.iloc[3, 1] = -998
# print(my_dataframe.iloc[0:3, 1])
print(my_dataframe)