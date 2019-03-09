import pandas as pd
cars = pd.read_csv('./DataResources/cars.csv', index_col = 0)

# Print country and drives_right column
print(cars.loc[:,['country','drives_right']])

# Print Japan, India, Russia's  row of drives_right column
print(cars.loc[['JAP','IN','RU'],['country','drives_right']])

# Print Japan, India, Russia's  row of all column
print(cars.loc[['JAP','IN','RU']])