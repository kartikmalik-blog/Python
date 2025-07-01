'''
Why Array Operations?
NumPy arrays support element-wise operations (e.g., adding or multiplying each element) and aggregation (e.g., sum, mean), which are faster and cleaner than Python loops.
These are useful for numerical tasks, like analyzing expenses in your Expense Tracker project.
'''
'''
Key Concepts
Element-wise Operations: Perform operations (e.g., +, *) on each element of an array without loops.
Aggregation: Compute statistics like sum, mean, max, min across an array.
Functions: Encapsulate operations in functions for reusability, using isinstance for validation (from our function lessons).
'''

#Example Code
import numpy as np


#Function to create a validated numpy array
def create_array(data, dtype="float"):
    if not all(isinstance(x, (int, float)) for x in data):
        return "Error: all elements must be numbers:"
    return np.array(data, dtype=dtype)

#Function for element wise operations
def array_operations(arr1, arr2, operation="add"):
    if not(isinstance(arr1, np.ndarray) and isinstance(arr2, np.ndarray)):
        return "Error: the input must be numpy array"
    if arr1.shape != arr2.shape:
        return "Error: the shape of arrays must be same"
    
    if operation == "add":
        return arr1 + arr2 
    elif operation == "multiply":
        return arr1 * arr2
    elif operation == "substract":
        return arr1 - arr2
    else:
        return "Error: Unsupported operation"
    
#Function for aggression
def array_stat(arr, stat="sum"):
    if not isinstance(arr, np.ndarray):
        return "Error: all inputs must be numpy array"
    
    if stat == "sum":
        return np.sum(arr)
    elif stat == "mean":
        return np.mean(arr)
    elif stat == "max":
        return np.max(arr)
    else:
        return "Error: Unsupported statistic"
    
#Example Usage
#Create arrays
arr1 = create_array([1,2,3])
arr2 = create_array([4,5,6])

#Element wise operation
print(array_operations(arr1,arr2,"add"))
print(array_operations(arr1,arr2,"multiply"))
print(array_operations(arr1,arr2,"substract"))
print(array_operations(1,[1,2,3], "add"))

#Aggression
print(array_stat(arr1, "sum"))
print(array_stat(arr1,"mean"))
print(array_stat(arr1, "max"))
print(array_stat([1,2,3], "sum"))


'''
Query: What Does Aggregation Do, and Does It Include Only Mean, Mode, and Max, or Also Median and Min?
What is Aggregation in NumPy?
Aggregation refers to computing a single value (a scalar) from an array by applying a function across all elements, such as summing, averaging, or finding extremes.

Aggregation reduces an array (e.g., [1, 2, 3]) to one value (e.g., sum=6, mean=2.0, max=3).
It’s useful for summarizing data, like calculating total expenses in your Expense Tracker project.
'''
def process_arrays(data1,data2,operation="add", dtype="float"):
    arr1= create_array(data1, dtype)
    arr2 = create_array(data1,dtype)
    if isinstance(arr1, str) or isinstance(arr2,str):
        return arr1 if isinstance(arr1, str) else arr2
    return array_operations(arr1,arr2,operation) 

print(process_arrays([1,2],[3,4], "sum",dtype=np.int32))
print(process_arrays([1,2],[3,4],"multiply", dtype=np.float32))
print(process_arrays([1,2], [2,"3"], "add"))
print(process_arrays([1,2], [3], "add"))

'''
Purpose of dtype: The dtype parameter in np.array(data, dtype) specifies the data type of the NumPy array’s elements (e.g., np.int32, np.float64). This controls how numbers are stored and displayed (e.g., integers vs. floats with decimals).
Why Use It in create_array:
In process_arrays, we pass data1 and data2 (Python lists) to create_array, along with the dtype parameter (default "float").
create_array uses np.array(data, dtype=dtype) to convert the list to a NumPy array with the specified type.
Example: create_array([1, 2, 3], dtype=np.int32) → [1 2 3] (integers, no decimals). create_array([1, 2, 3], dtype="float") → [1. 2. 3.] (floats with decimals).
'''
#converting the list into NumPy solo:-
def process_array(data1,data2,operation="add", dtype="float"):
    if not all(isinstance(x, (int,float)) for x in data1):
        return "Error: all inputs must be NumPy"
    arr1 = np.array(data1, dtype=dtype)

    if not all(isinstance(x, (int,float)) for x in data2):
        return "Error: all inputs must be NumPy"
    arr2 = np.array(data2, dtype=dtype)

    if arr1.shape != arr2.shape:
        return "Error: the shape of arrays must be same"

    return array_operations(arr1,arr2,operation)


print(process_array([1,2],[3,4], "add",dtype=np.int32))
print(process_array([1,2],[3,4], "multiply", dtype=np.int32))
print(process_array([1,2],[3,"4"], "add"))
print(process_array([1,2],[3], "add"))


    