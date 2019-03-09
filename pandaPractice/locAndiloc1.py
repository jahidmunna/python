# Import cars data
import pandas as pd
cars = pd.read_csv('./DataResources/cars.csv', index_col = 0)

# Print out observation/row for Japan
print(cars.loc[['JAP']])
# or cars.iloc[[2]

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
#or print(cars.iloc[[1,6]])
