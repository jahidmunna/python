import pandas as pd
cars = pd.read_csv('./DataResources/cars.csv', index_col = 0)

# Print country(#0 index) and drives_right(#2 index) column
print(cars.iloc[:,[0,1]])

# # Print country(#0 index) and drives_right(#2 index) column
# print(cars.iloc[:,:2].values)


# Print Japan (2), India (3), Russia's (4)  row of country, drives_right column
print(cars.iloc[[2,3,4],[0,1]])

# Print Japan, India, Russia's  row of all column
print(cars.iloc[[2,3,4]])