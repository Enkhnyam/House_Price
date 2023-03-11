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

corrmat = train_data.corr()
# plt.figure.Figure(figsize=(12, 9))
sns.set_context('paper', font_scale=1.2)
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat)

k = 10
cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
cm = np.corrcoef(train_data[cols].values.T)
sns.set(font_scale=1)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.3f', annot_kws={'size': 8}, yticklabels=cols.values, xticklabels=cols.values)
plt.show()

#scatterplot
sns.set()
cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
sns.pairplot(train_data[cols], height = 2.5)
plt.show();

#missing data
total = train_data.isnull().sum().sort_values(ascending=False)
percent = (train_data.isnull().sum()/train_data.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
# missing_data.head(20)
total.head(20)

# #dealing with missing data
# train_data = train_data.drop((missing_data[missing_data['Total'] > 1]).index,1)
train_data = train_data.drop(train_data.columns[train_data.apply(lambda col:col.isnull().sum()>1)], axis=1)
train_data = train_data.drop(train_data.loc[train_data['Electrical'].isnull()].index) # lets also delete that one observation that was missing in Electrical
train_data.isnull().sum().max() #just checking that there's no missing data missing...

saleprice_scaled = StandardScaler().fit_transform(train_data['SalePrice'][:,np.newaxis])
