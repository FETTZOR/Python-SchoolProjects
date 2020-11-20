import numpy as np
import pandas as pd

my_numpy_array = np.array([[18, 23, 43],[168, 168, 191]]).T

my_dataframe=pd.DataFrame(my_numpy_array, columns=["age", "hight"])
my_dataframe.head(10)

print(my_dataframe)