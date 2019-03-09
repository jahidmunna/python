# baseball is available as a regular list of lists
baseball = [[78.4, 180, 27],
            [102.7, 215, 28],
            [98.5, 210, 26],
            [75.2, 188, 24]]
# updated is available as 2D numpy array
updated = [[1, .6, 2],
            [2, .3, 1],
            [3, .5, 2],
            [1, .5, 0]]
# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(baseball+updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1]) # to convert the units of height and weight to metric (meters and kilograms respectively) 

# Print out product of np_baseball and conversion
print(np_baseball * conversion)