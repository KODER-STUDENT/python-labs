A = [
    [34, -8, 27, 7, 12],
    [-5, 23, 45, 67, -2],
    [13, -12, 34, -3, 25],
    [17, 56, -6, 17, 21],
    [0, 15, 4, 9, -14]
]

sorted_matrix = [sorted(row) for row in A]

min_elements = [min(column) for column in zip(*sorted_matrix)]

from functools import reduce
from operator import mul

product_of_min_elements = reduce(mul, min_elements)

print("Sorted Matrix:")
for row in sorted_matrix:
    print(row)

print("\nMinimum elements in each column:", min_elements)
print("Product of minimum elements:", product_of_min_elements)