import pandas as pd
import numpy as np
import seaborn as sns
# pd.set_option('display.width', 400)
# pd.set_option('display.max_columns', 550)
# pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# pd.set_option("display.max_rows", None, "display.max_columns", None)
data = pd.read_csv('data_by_year.csv')
#1
# my_dataframe = data.sort_values(by='year', ascending=False)
# # print(data1.head(3))
# # # 2
# my_dataframe.head(10)
data = data.drop(['acousticness', 'energy', 'instrumentalness', 'valence', 'popularity', 'key', 'mode'], axis=1)
# print(data.loc[15])
# print(data.head(20))
loudness_nowadays_counter = 0
loudness_before_counter = 0

data2 = data[['year', "loudness"]].groupby("year").mean()
loudness_value_1921 = data2.iloc[1].tolist()
loudness_value_1921 = ("".join(map(str, loudness_value_1921)))
loudness_value_1921 = ("".join(map(str, loudness_value_1921)))
loudness_value_1980 = data2.iloc[59].tolist()
loudness_value_1980 = ("".join(map(str, loudness_value_1980)))
loudness_value_2000 = data2.iloc[79].tolist()
loudness_value_2000 = ("".join(map(str, loudness_value_2000)))
loudness_value_2010 = data2.iloc[89].tolist()
loudness_value_2010 = ("".join(map(str, loudness_value_2010)))
loudness_value_2020 = data2.iloc[99].tolist()
loudness_value_2020 = ("".join(map(str, loudness_value_2020)))
print(loudness_value_2020)

# compare loudness values between 2020 and 1921
if float(loudness_value_1921) > float(loudness_value_2020):
    difference = float(loudness_value_1921) - float(loudness_value_2020)
    # print(f'Music in 1921 was louder then nowadays... and difference between them is {difference}\n'
    #       f'when average loudness in 1921 was {loudness_value_1921} and average loudness nowadays'
    #       f' {round(float(loudness_value_2020))}')
    loudness_before_counter += 1
else:
    difference = float(loudness_value_2020) - float(loudness_value_1921)
    # print(f'Music in 2020 was louder then in 1921... and difference between them is {round(difference, 2)}\n'
    #       f'when average loudness in 1921 was {round(float(loudness_value_1921))} and average'
    #       f' loudness nowadays {round(float(loudness_value_2020))}')
    loudness_nowadays_counter += 1

if float(loudness_value_1980) > float(loudness_value_2020):
    difference = float(loudness_value_1980) - float(loudness_value_2020)
    # print(f'Music in 1981 was louder then nowadays... and difference between them is {difference}\n'
    #       f'when average loudness in 1981 was {loudness_value_1980} and average loudness nowadays'
    #       f' {round(float(loudness_value_2020))}')
    loudness_before_counter += 1
else:
    difference = float(loudness_value_2020) - float(loudness_value_1980)
    # print(f'Music in 2020 was louder then in 1981... and difference between them is {round(difference, 2)}\n'
    #       f'when average loudness in 1981 was {round(float(loudness_value_1980))} and average'
    #       f' loudness nowadays {round(float(loudness_value_2020))}')
    loudness_nowadays_counter += 1
# loudness_value_1921 = data2.iloc[1].tolist()
data2["loudness_difference_between_nowadays"] = data2["loudness"] - float(loudness_value_2020)
# if np.isclose(data2["loudness_difference_between_nowadays"], data2["loudness"]) :
#     data2["loundness_in_word"] = "nowadays louder"
mask=(data2['loudness_difference_between_nowadays'] != 0.0) & (data2['loudness'] != 0.0) & (data2['loudness_difference_between_nowadays'] > data2['loudness'])
data2['loudness_difference_by_words'] = np.where(mask, 'nowadays louder', 'Not equal')

numeric_columns = ['loudness']
# sns_plot = sns.pairplot(data2[numeric_columns])
# sns_plot.savefig('pairplot.png')
# print(sns_plot)
hah = sns.distplot(data2[numeric_columns])
hah.savefig('asd.png')
# print(data2)

# my_list = data2["loudness"]
# print(my_list)

# high_scores1['is_score_chased'] = np.where(high_scores1['runs1']>=high_scores1['runs2'],
#                                            'yes', 'no')
# print(my_dataframe.drop(['first'], axis=1))
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
# five = data[['Genre', "Author"]].groupby("Author").count()
# five = five.sort_values(by='Genre', ascending=False)
# five.to_html('taskreallife5.html')