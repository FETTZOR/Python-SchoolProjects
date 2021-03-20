import pandas as pd
import numpy as np


data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
# 1
# print(data[['gender', "MonthlyCharges"]].groupby("gender").mean())
#
# #  2
# print(data[['Partner', "Churn"]].groupby("Partner").count())
#
# #  3
# print(data[["Churn", "Partner"]].groupby(["Partner"]).count() / data["Partner"].count() * 100)
#
# #  4
# print(data[['gender', "Partner"]].value_counts(normalize=True) * 100)

# print(data.groupby("Partner")["gender"].value_counts(normalize=True) * 100)

# 5
# mybad = data.groupby('gender')[['gender', 'InternetService']].agg(lambda x: x.value_counts().to_dict())
# print(mybad.head(1))
# females_with_fiber_percentage = 1553 / ((data['gender'].values == 'Female').sum() / 100)
# print(females_with_fiber_percentage)
# print(data[["gender","InternetService"]].groupby("gender")["InternetService"].get_group("Female").value_counts().\
#     to_frame("%")/data[["gender"]].groupby("gender").get_group("Female").value_counts().sum()*100)

# 6
# print(data[["gender", "Partner", "MonthlyCharges"]].groupby(["gender", "Partner"]).mean())
# # Calculate how many procentages of Females have "Fiber optic" as Internet Serveice
#
# # 7
# print(data[["gender", "Partner", "MonthlyCharges", "InternetService"]].
#       groupby(["gender", "Partner", "InternetService"]).mean())

# 8
data[["TotalCharges"]] = pd.to_numeric(data["TotalCharges"],errors='coerce')
data[["TotalCharges","Partner"]].groupby(["Partner"]).median()