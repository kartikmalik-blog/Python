'''
Why Indexing and Slicing?
Indexing and slicing let you access or modify specific elements, rows, or columns in a NumPy array.
Unlike Python lists, NumPy supports multi-dimensional indexing (e.g., arr[1, 2] for 2D arrays) and advanced slicing, which is faster and more flexible.
Useful for tasks like extracting specific expense amounts from your Expense Tracker data.
Key Concepts
Indexing: Access a single element (e.g., arr[0] for the first element).
Slicing: Access a subset of elements (e.g., arr[1:3] for elements at indices 1 and 2).
2D Arrays: Use arr[row, col] or arr[row_start:row_end, col_start:col_end] for multi-dimensional arrays.
Validation: Use functions to ensure valid indices/slices, tying to your function lessons.
'''
'''
Let’s create functions to perform indexing and slicing, incorporating validation (using isinstance and error checking from our function lessons) and building on create_array from numpy_operations.py.
'''

import numpy as np

# Function to create a validated NumPy array
def create_array(data, dtype="float"):
    # Check if all elements (including nested) are numbers
    def is_numeric(item):
        if isinstance(item, (int, float)):
            return True
        if isinstance(item, list):
            return all(is_numeric(x) for x in item)
        return False
    
    if not all(is_numeric(x) for x in data):
        return "Error: All elements must be numbers"
    # Check for consistent sublist lengths
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], list):
        if not all(len(sublist) == len(data[0]) for sublist in data):
            return "Error: All sublists must have the same length"
    return np.array(data, dtype=dtype)

# Function for indexing an array
def get_element(arr, index):
    if not isinstance(arr, np.ndarray):
        return "Error: Input must be a NumPy array"
    if not isinstance(index, (int, tuple)):
        return "Error: Index must be an integer or tuple"
    try:
        return arr[index]
    except IndexError:
        return "Error: Index out of bounds"

# Function for slicing an array
def get_slice(arr, row_slice=None, col_slice=None):
    if not isinstance(arr, np.ndarray):
        return "Error: Input must be a NumPy array"
    try:
        if arr.ndim == 1:
            slice_obj = slice(row_slice[0], row_slice[1], None) if isinstance(row_slice, tuple) else slice(row_slice, None, None)
            return arr[slice_obj]
        elif arr.ndim == 2:
            row_slice_obj = slice(row_slice[0], row_slice[1], None) if isinstance(row_slice, tuple) else slice(None)
            col_slice_obj = slice(col_slice[0], col_slice[1], None) if isinstance(col_slice, tuple) else slice(None)
            return arr[row_slice_obj, col_slice_obj]
        else:
            return "Error: Unsupported array dimensions"
    except (IndexError, TypeError):
        return "Error: Invalid slice parameters"

# Example usage
# 1D array
# arr1 = create_array([10, 20, 30, 40, 50])
# print("1D array:", arr1)  # Output: [10. 20. 30. 40. 50.]
# print("Index 2:", get_element(arr1, 2))  # Output: 30.0
# print("Slice 1:3:", get_slice(arr1, (1, 3)))  # Output: [20. 30.]

# 2D array
# arr2 = create_array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("2D array:\n", arr2)  # Output: [[1. 2. 3.] [4. 5. 6.] [7. 8. 9.]]
# print("Index (1, 2):", get_element(arr2, (1, 2)))  # Output: 6.0
# print("Slice rows 0:2, cols 1:2:", get_slice(arr2, (0, 2), (1, 2)))  # Output: [[2.] [5.]]

# Error cases
# print(get_element(arr1, 10))  # Output: Error: Index out of bounds
# print(get_slice(arr1, (1, 6)))  # Output: Error: Invalid slice parameters
# print(get_element([1, 2, 3], 0))  # Output: Error: Input must be a NumPy array
# print(create_array([[1, 2], [3, 4, 5]]))  # Output: Error: All sublists must have the same length

#Practice 
def extract_data(data, index=0,slice_params=None, dtype="float"):
    arr = create_array(data,dtype)
    if isinstance(arr, str):
        return arr
    if slice_params is not None:
        return get_slice(arr, *slice_params)
    return get_element(arr, index)

print(extract_data([10,20,30], index=1))
print(extract_data([[1,2],[3,4]], index=(1,0)))
print(extract_data([10,20,30,40], slice_params=(1,3)))
print(extract_data([1,"2"], index=0))
print(extract_data([1,2,3], index=5))

'''
What’s the difference between arr[1] and arr[1:2] for a 1D array?
Your Answer: “The difference between arr[1] and arr[1:2] is first is indexing and second is slicing.”
Confirmation: Correct!
arr[1] is indexing: It returns a single element (a scalar) at index 1. Example: For arr = np.array([10, 20, 30]), arr[1] → 20.0.
arr[1:2] is slicing: It returns a subarray (a NumPy array) with elements from index 1 up to (but not including) 2. Example: arr[1:2] → [20.] (a 1D array with one element).
Key Difference: arr[1] gives a single value (e.g., float), while arr[1:2] gives an array (even if it has one element), preserving the array structure.
Why does get_element(arr2, (1, 2)) use a tuple for a 2D array?
Your Answer: “The get_element(arr2, (1, 2)) uses a tuple for a 2D array because tuple is immutable I think.”
Confirmation: Partially correct, but let’s clarify:
Correct Part: A tuple is used for indexing 2D arrays in NumPy, like arr2[1, 2] or arr2[(1, 2)].
Why a Tuple?: NumPy uses tuples to specify multi-dimensional indices (e.g., (row, col) for 2D arrays). For arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), get_element(arr2, (1, 2)) accesses row 1, column 2 → 6.0. The tuple (1, 2) is a single argument that NumPy interprets as (row, col).
Immutable Aspect: Tuples are immutable, which is convenient (ensures the index isn’t accidentally modified), but the main reason is NumPy’s syntax: it expects a tuple for multi-dimensional indexing to separate dimensions clearly (e.g., arr[row, col]).
Example: arr2[1, 2] is equivalent to arr2[(1, 2)]. The tuple groups the indices for NumPy to process.
Why Not a List?: You could use a list like [1, 2], but NumPy converts it to a tuple internally. Tuples are standard for clarity and consistency.
What happens if you pass invalid slice_params (e.g., start=10)?
Your Answer: “When we pass invalid start=10 it gives error either invalid array dimensions, or invalid parameters.”
Confirmation: Mostly correct, but let’s be precise:
In get_slice(arr, row_slice, col_slice), if row_slice=(10, 12) for a 1D array arr = np.array([10, 20, 30]) (length 3), start=10 is out of bounds.
The get_slice function catches this in the try-except block and returns "Error: Invalid slice".
Why Not “Invalid array dimensions”?: The "Error: Unsupported array dimensions" error only occurs if the array has more than 2 dimensions (e.g., a 3D array). For start=10, it’s an IndexError caught as "Error: Invalid slice".
Example:
get_slice(arr1, (1, 6)) for arr1 = [10, 20, 30, 40, 50] → "Error: Invalid slice" (because stop=6 exceeds length 5).
get_slice(arr2, (0, 4), (1, 2)) for arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] → "Error: Invalid slice" (row stop=4 exceeds 3 rows).
'''