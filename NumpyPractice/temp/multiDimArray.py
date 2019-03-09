import numpy as np

twoDimentionalArray = np.array(
        [[1,2,3],
        [4,5,6],
        [7,8,9]]
    )

print(twoDimentionalArray)

# find the dimention number
numberOfDimention = twoDimentionalArray.ndim
print(numberOfDimention)

#shape
print(twoDimentionalArray.shape)