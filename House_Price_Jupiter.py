# importing all the necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# importing the dataset
train_data = pd.read_csv('train.csv')
train_data

# taking a look at the columns
train_data.columns

# I thought intuitively that the SalePrice should be the most relevant and important factor
# so I started with it. To learn more about SalePrice feature lets use describe
train_data['SalePrice'].describe()

# we can see that this feature:
# Deviate from the normal distribution.
# Have appreciable positive skewness.
# Show peakedness.
sns.distplot(train_data['SalePrice'])

#skewness and kurtosis
print("Skewness: %f" % df_train['SalePrice'].skew())
print("Kurtosis: %f" % df_train['SalePrice'].kurt())


# I switched between a few features and found these two to be most linearly related
# var = 'GrLivArea'
var1 = 'TotalBsmtSF'
data = pd.concat([train_data['SalePrice'], train_data[var1]], axis=1)
data.plot.scatter(x=var1,y='SalePrice',ylim=(0,800000))

# Lets see if the Overall quality of the house is related with the price
var2 = 'OverallQual'
data = pd.concat([train_data['SalePrice'], train_data[var2]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig=sns.boxplot(x=var2, y='SalePrice', data=data)
fig.axis(ymin=0, ymax=800000)

# How about YearBuilt
var3 = 'YearBuilt'
data = pd.concat([train_data['SalePrice'], train_data[var3]], axis=1)
f, ax = plt.subplots(figsize=(16, 8))
fig = sns.boxplot(x=var3, y="SalePrice", data=data)
fig.axis(ymin=0, ymax=800000)
plt.xticks(rotation=90)
