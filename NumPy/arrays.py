# Step 1: Introduction to NumPy and Array Creation
# Why NumPy?
# NumPy (Numerical Python) is a library for efficient numerical computations, primarily using arrays.
# It’s faster than Python lists for math operations (e.g., addition, multiplication) and essential for data science, machine learning, and your upcoming numerical tasks.
# Builds on your Python knowledge (loops, functions, data structures) but simplifies operations on large datasets.

#Key Concept: NumPy Arrays
#NumPy’s core is the ndarray (n-dimensional array), a fast, memory-efficient data structure for numerical data.
#Unlike Python lists, arrays have a fixed type (e.g., int, float) and support element-wise operations.

import numpy as np

#Function to create and return numpy array from a list
'''def create_array(data):
    if not all(isinstance(x, (int,float)) for x in data):
        return "Error: all elements must be numbers"
    return np.array(data)

#Example usage
print(create_array([1, 2, 3, 4]))
print(create_array([1, "2", 3]))

#other ways to create arrays
def explore_array():
    #1D array from range
    arr1 = np.arange(5) #[0,1,2,3]
    #2D array from zeros
    arr2 = np.zeros((2,3)) #[[0.0.0], [0.0.0]]
    #Array with evenly spaced values
    arr3 = np.linspace(0, 10, 5) #[0. 2.5 5.   7.5  10.]
    return arr1, arr2, arr3

#Test the function
arr1, arr2, arr3 = explore_array()
print("1D array:", arr1)
print("zeros array:", arr2)
print("linespace array:", arr3)'''

'''Query 1: How Does x Work in isinstance Without Passing It as a Parameter?
Question: In isinstance(x, (int, float)) for x in data, how does x work if we only pass data to the function?

Answer:

The x is a loop variable used in the list comprehension inside the all() function.
In create_array(data), data is a list (e.g., [1, 2, 3, 4]).
The expression all(isinstance(x, (int, float)) for x in data) iterates over each element in data, assigning it to x one at a time.
For data = [1, 2, 3, 4], x takes on values 1, 2, 3, 4 in each iteration.
isinstance(x, (int, float)) checks if x is an integer or float.
The for x in data part is a generator expression that loops through data without explicitly defining x as a parameter in the function signature—it’s created by the loop.
all(...) returns True only if every element in data passes the isinstance check; otherwise, it returns False, triggering the error message.
Example:

For create_array([1, 2, 3]):
x becomes 1, isinstance(1, (int, float)) → True.
x becomes 2, isinstance(2, (int, float)) → True.
x becomes 3, isinstance(3, (int, float)) → True.
all(...) → True, so np.array([1, 2, 3]) is returned.

For create_array([1, "2", 3]):
x becomes "2", isinstance("2", (int, float)) → False.
all(...) → False, so returns "Error: All elements must be numbers".
In Short: x is a temporary variable created by the for x in data loop to check each element in data. You don’t pass x explicitly; it’s generated when iterating over data.'''

'''
Query 2: How Does np.array(data) Work?
Question: How does np.array(data) convert the input list to a NumPy array?

Answer:

np.array(data) is a NumPy function that takes a Python list (or other iterable, like data) and creates a NumPy ndarray (n-dimensional array).
It converts the list into a fixed-type, efficient array optimized for numerical operations.
How it works:
It reads the elements of data (e.g., [1, 2, 3, 4]) and determines a common data type (dtype), usually int or float for numbers.
It creates a contiguous block of memory to store the elements, unlike Python lists, which are scattered in memory.
The resulting array supports fast math operations (e.g., element-wise addition) and has attributes like shape and dtype.
Example:

data = [1, 2, 3, 4] → np.array(data) creates [1 2 3 4] with dtype=int32 or int64 (depending on your system).
data = [1.0, 2.5, 3.0] → np.array(data) creates [1. 2.5 3. ] with dtype=float64.
If mixed types (e.g., [1, "2", 3]), NumPy tries to coerce to a common type (e.g., strings), but our isinstance check prevents this by returning an error first.
In Short: np.array(data) converts a list to a NumPy array by assigning a uniform data type and storing elements efficiently for numerical tasks.

'''

'''
Query 3: How Does np.zeros Work?
Question: Explain the np.zeros array in np.zeros((2, 3)).

Answer:

np.zeros(shape) creates a NumPy array filled with zeros, with the specified shape (a tuple of dimensions).
In np.zeros((2, 3)):
(2, 3) means a 2D array with 2 rows and 3 columns.
All elements are set to 0.0 (float type, by default).
Output: [[0. 0. 0.], [0. 0. 0.]] (a 2x3 matrix of zeros).
Why use it? To initialize arrays for calculations (e.g., placeholders for data in your Expense Tracker).
Example:

np.zeros((2, 3)) → [[0. 0. 0.], [0. 0. 0.]] (2 rows, 3 columns).
np.zeros(4) → [0. 0. 0. 0.] (1D array of length 4).
You can specify dtype, e.g., np.zeros((2, 3), dtype=int) → [[0 0 0], [0 0 0]].
In Short: np.zeros((2, 3)) creates a 2x3 array filled with 0.0, useful for initializing matrices.
'''

'''
Query 4: How Does np.linspace Work?
Question: Explain the np.linspace array in np.linspace(0, 10, 5).

Answer:

np.linspace(start, stop, num) creates a 1D NumPy array with num evenly spaced values from start to stop (inclusive).
In np.linspace(0, 10, 5):
start=0, stop=10, num=5 means 5 values evenly spaced from 0 to 10.
It calculates: (stop - start) / (num - 1) = (10 - 0) / (5 - 1) = 2.5 as the step size.
Output: [0. 2.5 5. 7.5 10. ] (5 values, including 0 and 10).
Why use it? For creating sequences for plots, simulations, or numerical analysis (e.g., time intervals in your projects).
Example:

np.linspace(0, 10, 5) → [0. 2.5 5. 7.5 10. ].
np.linspace(1, 5, 3) → [1. 3. 5. ] (3 values from 1 to 5).
In Short: np.linspace(0, 10, 5) creates an array of 5 evenly spaced values from 0 to 10, inclusive, with a step size of 2.5.
'''


#Practice task
'''def make_array(data, dtype=float):
    if not all(isinstance(x, (int, float)) for x in data):
        return "Error: all elements must be numbers"
    return np.array(data, dtype=dtype)

print(make_array([1, 2, 3]))
print(make_array([1, 2, 3], dtype=np.int32))
print(make_array([1, "2", 3]))
print(make_array([1, 2, 3], dtype=np.float64))'''


