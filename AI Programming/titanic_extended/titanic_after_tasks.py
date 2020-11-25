import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

data = pd.read_csv('Titanic_extended.csv')
data = data.drop(["Name", "Ticket", "Name_wiki", "Body"], axis=1)
data = data.rename(columns={"PassengerId": "id"})
# data = data.reindex(columns=['Id','Pclass','Sex','Age',
#                              'Age_wiki','Class','SibSp',
#                              'Parch','Fare','Cabin',
#                              'Embarked','Hometown',
#                              'Boarded','Destination',
#                              'Lifeboat','WikiId','Survived'])

data = data[["id", "Pclass", "Sex", "Age", "Age_wiki", "Class", "SibSp", "Parch", "Fare",
             "Cabin", "Embarked", "Hometown", "Boarded",
             "Destination", "Lifeboat", "WikiId", "Survived"]]
# print(data.head())
data.to_csv('Titanic_extended_2.csv', index=False)
data["Age"].mean()
data["Fare"].median()
# print((data["Survived"].sum(axis=0))/891*100)
# print((data["Survived"].mean()*100))
survived_col = data["Survived"].value_counts()
survived_per = (survived_col[1] / sum(survived_col)) * 100
# print(f"{survived_per:.2f}% survived")
# print(data.head(3))

print(data["Fare"].sum())
# How much money did all pasengers pay altogether as ticket Fares?

# Remove columns : "Name", "Ticket", "Name_wiki", "Body"
# Rename column "PassengerId" as id
# Find out how to change the order of the columns in a dataframe and reorder it like in image below.
# Save the dataframe as "Titanic_extended_2.csv
# Find out hot to calculate the mean of the column "Age"
# Find out what "median" means and how to calculate the median of the column "Fare"
# How many procentage of all pasengers survived?
# How much money did all pasengers pay altogether as ticket Fares?
