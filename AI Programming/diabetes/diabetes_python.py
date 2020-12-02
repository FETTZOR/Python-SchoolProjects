import pandas as pd

data = pd.read_csv('diabetes.csv')
data_shape = data.shape
data_size = data.size

print(data.describe(percentiles=[.90]))
