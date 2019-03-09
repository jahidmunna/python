# Pre-defined lists treat as column
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
# this dic treats as column name
my_dict = { 
    'country':names, 
    'drives_right':dr,
    'cars_per_cap':cpc 
}

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict, index=row_labels)

# Print cars
print(cars)
