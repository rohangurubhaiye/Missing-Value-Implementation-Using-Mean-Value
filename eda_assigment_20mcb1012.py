# -*- coding: utf-8 -*-
"""EDA_Assigment-20MCB1012.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iWfcgpuPJcuCxglQxDA9Q6ZIfo6vujUu

**Name:-Rohan Gurubhaiye**

> 


**Reg no:- 20MCB1012**

>
**Description Of Assignment :-** 
>
 In this Assignment i have used Titanic Dataset which is having two Column Age and Cabin with missing Values, I have used mean value imputation method to fill missing value.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""To read the Dataset."""

titanic=pd.read_csv('/content/titanic.csv')

"""View Top Five Record of Column"""

titanic.head()

"""We Can Use Plot to view the missing values in the table titanic"""

plt.figure(figsize=(12, 7)) #increase the size of graph.
sns.heatmap(titanic.isnull(),yticklabels=False,cbar=False)

"""Roughly 20 percent of the Age data is missing. The proportion of Age missing is likely small enough for reasonable replacement with some form of imputation. Looking at the Cabin column, it looks like we are just missing too much of that data to do something useful with at a basic level."""

plt.figure(figsize=(12, 7))
sns.boxplot(x='Pclass',y='Age',data=titanic)

"""Overview of Column Age with respect to ticket class i.e Pclass column

lets find the average age of the passengers of each class
"""

titanic[['Age','Pclass']].groupby('Pclass').mean()

"""We got Average Age of the Passengers based on the class of ticket


1.   We Can see That Passengers Having First Class Ticket are about 38 Years Old roughly.
2.   We Can see That Passengers Having Second Class Ticket are about 29 Years Old roughly.
3.   We Can see That Passengers Having Third Class Ticket are about 25 Years Old roughly.

I am going to use average of the age based on the ticket class to perform missing values imputation on age column.
"""

def impute_Age(cols):    #the data from respective column i.e Age,Pclass will be passed here
  Age = cols[0]          #retrieve the value in age column 
  Pclass = cols[1]       #retrieve the value in Pclass column for determining class of ticket
  if pd.isnull(Age):     #if the value in the age is foun null at any record in age the it will execute
      if Pclass == 1:    #if the ticket class or Pclass is 1 the value of age will be 38
          return 38    
      elif Pclass == 2:  #if the ticket class or Pclass 2 is  the value of age will be 29
          return 29
      else:              #if the ticket class or Pclass is 3 the value of age will be 25
          return 25
  else:
      return Age         #if Value is not null the it will return the passed value without any modification.

"""The Above fucntion will fill the Missing value based on the average age of the passenger based on their class"""

titanic['Age'] = titanic[['Age','Pclass']].apply(impute_Age,axis=1) #here the function Impute Age will be applied on each row of column Age.

"""The Apply Function will apply the function we developed on column Age. In above code Axis  Represents the Column."""

plt.figure(figsize=(12, 7)) #increase the size of graph.
sns.heatmap(titanic.isnull(),yticklabels=False,cbar=False)

"""As you can see in the above plot there are no longer null value Availabe in Column Age, After missing value imputation using average age based on pclass.

As the Column Cabin have too much of Missing valuees we will Simply Drop the Column.
"""

titanic.drop('Cabin',axis=1,inplace=True) #inplace= true will reflect in the changes in main titanic dataframe.

titanic.info()

plt.figure(figsize=(12, 7)) #increase the size of graph.
sns.heatmap(titanic.isnull(),yticklabels=False,cbar=False)

"""In the above heatmap Plot you can now see there are no missing values in the titanic dataframe."""

titanic

"""Lets Export the Clean DataSet."""

titanic.to_csv(r'/content/titanic_clean.csv', index = False)  #index is set to false as we dont need index column

