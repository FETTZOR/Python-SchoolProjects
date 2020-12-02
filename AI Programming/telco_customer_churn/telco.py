import pandas as pd
import numpy as np

data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
# print(data[['gender', "MonthlyCharges"]].groupby("gender").mean())
# print(data[['Partner', "Churn"]].groupby("Partner").count())
# data.head(3)

sum_of_data = data[['Partner', "Churn"]].groupby("Partner").count().sum()
# print(data[['Partner', "Churn"]].groupby("Partner").count())
# sum_of_data_one_percent = sum_of_data / 100
# sum_of_data_no = (sum_of_data - 3402) / sum_of_data_one_percent
# sum_of_data_yes = (sum_of_data - 3641) / sum_of_data_one_percent
# print('Yes', sum_of_data_yes, '%')
# print('No', sum_of_data_no, '%')
#
# female = data[['gender', "Partner"]].groupby("gender").count()
# female_sum = data[['gender', "Partner"]].groupby("gender").count().sum() / 100
# female_one_percent = female_sum / 100
# print(female)
# print(female_sum)
# female_percentage = (female_sum - 3555) / female_one_percent
# print(female_percentage)

# print(data[["Churn","Partner"]].groupby(["Partner"]).count()/data["Partner"].count()*100)
# data[["Partner","Churn"]].groupby("Partner").count()
int_service_data = data.groupby('gender')['InternetService'].value_counts()
fem_fiber_per = int_service_data["Female"]["Fiber optic"] / int_service_data["Female"].sum() * 100
print(fem_fiber_per)
print(data[['gender', "InternetService"]].value_counts(normalize=True) * 100)
