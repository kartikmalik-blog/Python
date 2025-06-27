# # # def greet(name):
# # #     message = f"Hello {name}!"
# # #     return message
# # # result = greet("Kartik")
# # # print(result)

# # def add_numbers(a,b):
# #     # return a+b

# #     print(add_numbers(a,b))
# #     # print(add_numbers(5,-1))

# def add_numbers(a,b):
#     if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
#         raise ValueError("Input must be numbers")
#     return a + b

# print(add_numbers(6,7))
# print(add_numbers("hello", 7))

# def add_numbers(a,b):
#     if not (isinstance(a, (int,float)) and isinstance(b, (int,float))):
#         return "Error: both values must be numericals"
#     return a + b

# print(add_numbers(4,6))
# print(add_numbers("hello", 6))
# print(add_numbers(5.6, 6))

# def add_numbers(a, b, multiplier=1):
#     if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(multiplier, (int, float))):
#         return "Error: All inputs must be numbers"
#     return (a + b) * multiplier

# # Test cases
# print(add_numbers(3, 4))              # Uses default multiplier=1, Output: 7
# print(add_numbers(3, 4, 2))           # Output: 14 (i.e., (3 + 4) * 2)
# print(add_numbers(3, 4, multiplier=3)) # Keyword argument, Output: 21 (i.e., (3 + 4) * 3)
# print(add_numbers(a=2, b=5, multiplier=2)) # All keyword args, Output: 14
# print(add_numbers("hello", 5))        # Output: Error: All inputs must be numbers
 
# def append_to_list(items, my_list=[]):
#     my_list.append(items)
#     return my_list

# print(append_to_list(1))
# print(append_to_list(3))

# def append_to_list(items, my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append(items)
#     return my_list

# print(append_to_list(1))
# print(append_to_list(3))

def add_to_cart(items, cart=None):
    if not isinstance(items, str):
        return "Error: the items must string"
    if cart is None:
        cart = []
    cart.append(items)
    return cart

print(add_to_cart("banana"))
print(add_to_cart("apple"))
print(add_to_cart("grapes", ["milk"]))
print(add_to_cart(124))