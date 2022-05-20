from collections import Counter

X = 10

shoe_size = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]

num_shoes_each_size = Counter(shoe_size)
num_shoes_each_size[6] -=2 
print(f"num_shoes_each_size: {num_shoes_each_size[6]}")