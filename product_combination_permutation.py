
from itertools import product, permutations, combinations

# # First Make Set with N values
# SET = 'ABC'
# N = 2

# # Get Products
# print(f"product: {list(product(SET, repeat=N))}")

# # Get Permutations (Order Matters)
# print(f"permutations: {list(permutations(SET, N))}")

# # Get Combinations (Order Doesn't Matter)
# print(f"combinations: {list(combinations(SET, N))}")


A = [1, 2]
B = [3, 4]

c = [A, B]
print(f"c: {c}")
print(f"product: {list(product(*c))}")
print(f"product2: {list(product(A,B))}")
