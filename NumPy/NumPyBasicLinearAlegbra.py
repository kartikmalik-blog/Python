'''
Basic Linear Algebra
Why: Linear algebra operations like dot product (np.dot) are useful for calculations in projects (e.g., total expenses with tax rates or weighted sums).

Key Concept:

Dot Product: Multiplies arrays element-wise and sums the results (e.g., np.dot([1, 2], [3, 4]) → 1*3 + 2*4 = 11).
'''

import numpy as np

def compute_dot_products(data1,data2,scale=1):
    try:
        if not isinstance(scale,(int,float)):
            return "Error: the scale input must be numbers"
        arr1 = np.array(data1,dtype=float)
        arr2 = np.array(data2,dtype=float)
        if arr1.shape != arr2.shape:
            return "Error: the shape of arrays must be same"
        return np.dot(arr1,arr2) * scale
    except(ValueError, TypeError):
        return "Error: Invalid data"
    
print(compute_dot_products([1,2],[3,4]))
print(compute_dot_products([10,20,30],[1,2,3]))
print(compute_dot_products([10,20,30],[1,2,3], scale=2))
print(compute_dot_products([1,2],[1,2,3]))
print(compute_dot_products([1,"2"],[3,4]))