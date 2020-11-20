import numpy as np
import pandas as pd

my_numpy_array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(my_numpy_array)

my_dataframe=pd.DataFrame(my_numpy_array)
my_dataframe.head(10)