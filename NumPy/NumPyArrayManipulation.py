'''
Array Manipulation
Why: Reshaping organizes data (e.g., expenses into tables), concatenation merges datasets, and boolean indexing filters data (e.g., expenses > $50).

Key Concepts:
Reshaping: Change array shape (e.g., np.reshape(arr, (2, 3))).
Concatenation: Combine arrays (e.g., np.concatenate([arr1, arr2])).
Boolean Indexing: Filter with conditions (e.g., arr[arr > 50]).
'''
import numpy as np

def manipulate_array(data, data2=None, shape=None, condition=None, reverse=False):
    try:
        arr = np.array(data, dtype=float)
        if data2 is not None:
            arr2 = np.array(data2, dtype=float)
            arr = np.concatenate((arr, arr2))
        if shape is not None:
            arr = arr.reshape(shape)
        if condition is not None:
            arr = arr[arr > condition]
        if reverse:
            arr = np.flip(arr)
        return arr
    except (ValueError, TypeError):
        return "Error: Invalid operation"

# Test cases
print(manipulate_array([1, 2, 3, 4, 5, 6], shape=(2, 3)))  # [[1. 2. 3.] [4. 5. 6.]]
print(manipulate_array([10, 20], [30, 40], condition=25))  # [30. 40.]
print(manipulate_array([1, 2], [3, 4], shape=(2, 2)))  # [[1. 2.] [3. 4.]]
print(manipulate_array([1, 2], [3], shape=(2, 2)))  # Error: Invalid operation
print(manipulate_array([1, 2, 3], reverse=True))  # [3. 2. 1.]

'''
How manipulate_array Works
The function takes a list (data), an optional second list (data2), a shape for reshaping, a condition for filtering, and a reverse flag, then applies NumPy operations. Here’s each part:

Convert to NumPy Array:
arr = np.array(data, dtype=float):
Turns data (e.g., [1, 2, 3]) into a NumPy array with float type (e.g., [1. 2. 3.]).
Why: Ensures consistent data type for operations.
Concatenation (data2):
if data2 is not None: arr2 = np.array(data2, dtype=float); arr = np.concatenate((arr, arr2)):
Converts data2 to a NumPy array and merges it with arr.
Example: [1, 2] + [3, 4] → [1. 2. 3. 4.].
np.concatenate((arr, arr2)): Combines arrays along their first axis (1D arrays become one longer array).
Why: Merges datasets (e.g., expenses from different months).
Reshaping (shape):
if shape is not None: arr = arr.reshape(shape):
Changes the array’s shape (e.g., [1, 2, 3, 4, 5, 6] to [[1, 2, 3], [4, 5, 6]] with shape=(2, 3)).
Requires the total number of elements to match (e.g., 6 elements for 2x3).
Example: manipulate_array([1, 2, 3, 4, 5, 6], shape=(2, 3)) → [[1. 2. 3.] [4. 5. 6.]].
Why: Organizes data into tables (e.g., expenses by category/week).
Boolean Indexing (condition):
if condition is not None: arr = arr[arr > condition]:
Filters elements greater than condition.
Example: [10, 20, 30, 40] with condition=25 → [30. 40.].
Why: Extracts relevant data (e.g., expenses > $50).
Reverse (reverse):
if reverse: arr = np.flip(arr):
Reverses the array’s order.
Example: [1, 2, 3] with reverse=True → [3. 2. 1.].
Why: Useful for sorting or reversing time-based data (e.g., latest expenses first).
Error Handling:
try-except (ValueError, TypeError):
Catches errors (e.g., invalid reshape, non-numeric data) and returns "Error: Invalid operation".
Example: [1, 2] + [3] reshaped to (2, 2) fails (3 elements can’t fit 2x2).

Question 1: Why (2, 3) for Shape, and What If the Number of Elements Is Odd?
How (2, 3) Works:
The shape parameter in arr.reshape(shape) specifies the desired dimensions of the array (e.g., (rows, columns) for 2D).
(2, 3) means reshape the array into 2 rows and 3 columns, requiring 2 * 3 = 6 elements.
Example: manipulate_array([1, 2, 3, 4, 5, 6], shape=(2, 3)) → [[1, 2, 3], [4, 5, 6]].
The input list [1, 2, 3, 4, 5, 6] has 6 elements, which fits perfectly into a 2x3 array.
What If the Number of Elements Is Odd?:
If the number of elements doesn’t match the shape’s total size (rows * columns), reshaping fails with a ValueError.
Example: [1, 2, 3] (3 elements, odd) with shape=(2, 2) (needs 4 elements):
manipulate_array([1, 2, 3], shape=(2, 2)) → "Error: Invalid operation".
Why: 3 elements can’t fill a 2x2 array (4 slots).
Solutions for Odd Numbers:
Use a shape that matches the number of elements. For 3 elements:
(1, 3) → [[1, 2, 3]] (1 row, 3 columns).
(3, 1) → [[1], [2], [3]] (3 rows, 1 column).
Pad the array with extra values (e.g., np.pad) to make it even, but this wasn’t in the task.
Example: manipulate_array([1, 2, 3], shape=(1, 3)) → [[1, 2, 3]] works.
For Projects: In your Expense Tracker, if you have an odd number of expenses (e.g., [100, 50, 200]), reshape to (3, 1) or (1, 3) for analysis, not (2, 2).
Question 2: Explain Boolean Indexing Again
What It Does:
The line if condition is not None: arr = arr[arr > condition] filters elements in arr that are greater than condition.
Boolean Indexing: Creates a boolean array (True/False) for each element based on the condition, then selects only elements where True.
Example: arr = np.array([10, 20, 30, 40]), condition=25:
arr > 25 → [False, False, True, True] (10 and 20 are ≤ 25, 30 and 40 are > 25).
arr[arr > 25] → [30, 40] (selects elements where condition is True).
In manipulate_array([10, 20], [30, 40], condition=25):
Concatenates to [10, 20, 30, 40].
Filters with arr[arr > 25] → [30, 40].
'''