# Code all steps 1-5, one step at a time, so that all steps are visible in the code.
#
# TIP : Watch the time! Remember to copy paste your code and send the answer before time runs out!
#
# 1. Start by creating the DataFrame below.
# 2. then add a new column “third” with values 21-30
# 3. then add a new column “fourth” with values 40-31
# 4. then drop the “first” column by it’s name (not by index)
# 5. then rename the “second” column as “SECOND”
# 6. Copy the whole code to the answer field


#   first    second
# 0    1            11
# 1    2            12
# 2    3            13
# 3    4            14
# 4    5            15
# 5    6            16
# 6    7            17
# 7    8            18
# 8    9            19
# 9    10          20
import numpy as np
import pandas as pd

x = np.arange(10, dtype=int)
a = np.arange(10, 20, 1, dtype=int)
la = np.arange(21, 31, 1, dtype=int)
hh = np.arange(40, 30, -1, dtype=int)
my_numpy_array = np.array([x, a, la, hh]).T

my_dataframe = pd.DataFrame(my_numpy_array, columns=["first", "second", "third", "fourth"])
my_dataframe.head(10)

print(my_dataframe)
# 4
print(my_dataframe.drop(['first'], axis=1))

# 5
my_dataframe.columns = ["first", "SECOND", "third", "fourth"]

print(my_dataframe)

