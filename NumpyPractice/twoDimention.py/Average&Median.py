# baseball is available as a regular list of lists
baseball = [[78.4, 180, 27],
            [102.7, 215, 28],
            [98.5, 210, 26],
            [75.2, 188, 24]]

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]  # np_height_in  is equal to first column of np_baseball.

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))