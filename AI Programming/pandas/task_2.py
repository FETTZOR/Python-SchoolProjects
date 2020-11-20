import numpy as np
import pandas as pd

my_numpy_array = np.array([[29.0, 23.6, 43.5], [83.0, 92.0, 88.0], ["woman", "man", "woman"]]).T

my_dataframe=pd.DataFrame(my_numpy_array, columns=["bmi", "waist", "sex"])
my_dataframe.head(10)

print(my_dataframe)