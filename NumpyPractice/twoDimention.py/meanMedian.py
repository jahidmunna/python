# baseball is available as a regular list of lists
baseball = [[78.4, 180, 27],
            [102.7, 215, 28],
            [98.5, 210, 26],
            [75.2, 188, 24]]

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))


# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))