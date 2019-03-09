# Import cars data
import pandas as pd
cars = pd.read_csv('./DataResources/cars.csv', index_col = 0)

# Print out observations for Australia and Egypt
#print(cars.loc[['AUS', 'EG']])
#or print(cars.iloc[[1,6]])

# Print out drives_right value of Morocco
print(cars.loc['MOR','drives_right'])
# OR print(cars["drives_right"]['MOR'])
  
# Print out a sub-DataFrame, 
# containing the observations for Russia and Morocco and 
# the columns country and drives_right.
print(cars.loc[['RU','MOR'],['country','drives_right']],"\n")
#or print(cars.iloc[[4,5], [0,1]])

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])
