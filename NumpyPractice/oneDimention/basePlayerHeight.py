# import numpy
import numpy as np
# import resourse  from mspack
# import sys

# sys.path.append("g:\\CodePracticing\\pythonCode\\mspack")
# # sys.path.insert(0, 'g:\\CodePracticing\\pythonCode\\mspack')
# from baseballplayerdata import name, age, height

from  mspack.baseballplayerdata import name, age, height
# import model from different
# Create a numpy array from height_in: np_height_in
height_in = height
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254  # convert from inchi to meter

# Print np_height_m
print(np_height_m)

import pandas as pd 

column_label = {
    'Name': name,
    'Age': age,
    'Height': height
} 

table  = pd.DataFrame(column_label)

print(table)