import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.externals import joblib
import math

# Data Read 
df = pd.read_csv('./DataResources/homeprices.csv')

# Data pre-pocess 
# Fill all NaN field with the median of that column
bedrooms_median = math.floor(df['bedrooms'].median())
df['bedrooms'] = df['bedrooms'].fillna(bedrooms_median)

reg = linear_model.LinearRegression()
# Train with data 1st all independent features, 2nd the goal feature 
reg.fit(df[['area','bedrooms', 'age']],df['price'])

print(reg.coef_)
print(reg.intercept_)

#Now Prediction using area, bedrooms, and age
print(reg.predict([[3200, 3, 20]]))

#save the training model in a module
joblib.dump(reg,'linearRegression_model')

# use saved model to predict data
model = joblib.load('linearRegression_model')
print(model.predict([[3200, 3, 20]]))
