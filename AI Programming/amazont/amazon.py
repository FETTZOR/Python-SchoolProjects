import pandas as pd
import numpy as np
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
data = pd.read_csv('bestsellers with categories.csv')
#1
data1 = data.sort_values(by='User Rating', ascending=False)
# print(data1.head(3))
data1.to_html('taskreallife1.html')
# # 2
# data2 = data.sort_values(['User Rating', 'Reviews'], ascending=[False, False])
# print(data2.head(10))
# data2.to_html('taskreallife2.htm')
#
# new = data[['Genre', "Price"]].groupby("Genre").mean()
# # new = 14.84/10.85
#
# new.to_html('taskreallife3.html')
# file1 = open("myfile.txt", "w")
#
# file1.write("1.367741935483871")
# file1.close()  # to change file access modes
# # 4
five = data[['Genre', "Author"]].groupby("Author").count()
five = five.sort_values(by='Genre', ascending=False)
five.to_html('taskreallife5.html')
print(five)
