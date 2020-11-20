import numpy as np
import pandas as pd
x = np.arange(10, dtype = int)
a = np.arange(11, 21, 1, dtype=int)
my_numpy_array = np.array([x, a]).T

my_dataframe=pd.DataFrame(my_numpy_array, columns=["first", "second"])
my_dataframe.head(10)

print(my_dataframe)