import numpy as np

x = np.array([(1,2,3,4),(5,6,7,8)])
dymentionOfArray = x.ndim
#print(dymentionOfArray)

dataType = x.dtype
#print(dataType)

numberOfItem = x.itemsize
#print(numberOfItem)

sizeOfArray = x.size 
#print(sizeOfArray)

shapeOfArray = x.shape
#print(shapeOfArray)

y = x.reshape(4,2)
print(y)