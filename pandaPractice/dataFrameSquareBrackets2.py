# Import cars data
import pandas as pd
cars = pd.read_csv('./DataResources/cars.csv', index_col = 0)

# Print out first 3 observations/rows
print(cars[:3])

# Print out fourth, fifth and sixth observation
print(cars[4:7])
