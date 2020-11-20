import numpy as np
import pandas as pd

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

print(my_dataframe)
