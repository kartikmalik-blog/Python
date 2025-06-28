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

# def add_to_cart(items, cart=None):
#     if not isinstance(items, str):
#         return "Error: the items must string"
#     if cart is None:
#         cart = []
#     cart.append(items)
#     return cart

# print(add_to_cart("banana"))
# print(add_to_cart("apple"))
# print(add_to_cart("grapes", ["milk"]))
# print(add_to_cart(124))

# budget = 100 #Glocal varaible

# def deducte_expense(amount):
#     local_result = budget - amount #Reads Global budget, local result is local
#     return local_result

# print(deducte_expense(30))
# print(budget) #global unchanged 

#modifying global (avoid unless its neccessary)
# budget = 100

# def update_budget(amount):
#     global budget
#     budget -= amount
#     return budget

# print(update_budget(30))
# print(budget)

# def track_spending(category, *amounts, **options):
#     if not isinstance(category, str):
#         return "Error: Category must be a string"
#     if not all(isinstance(amount, (int, float)) for amount in amounts):
#         return "Error: All amounts must be numbers"
#     total = sum(amounts)
#     if options.get("tax_rate"):
#         total *= (1 + options["tax_rate"])
#     return total

# print(track_spending("food", 10, 20, 30))           # Output: 60.0
# print(track_spending("travel", 100, tax_rate=0.1))  # Output: 110.0
# print(track_spending(123, 10))                     # Output: "Error: Category must be a string"
# print(track_spending("food", 10, "20"))            # Output: "Error: All amounts must be numbers"

# def track_spending(category, *amounts, **options):
#     if not isinstance(category, str):
#         return "Error: the value must be string"
#     if not all(isinstance(amount, (int,float)) for amount in amounts):
#         return "Error: all values must be numeric"
#     descriptions = options.get("descriptions")
#     if descriptions is not None and not isinstance(descriptions, str):
#         return "Error: Description must be string"
#     total = sum(amounts)
#     if options.get("tax_rate"):
#         total *= (1 + options["tax_rate"])
#     if descriptions:
#         return{"category": category, "total": total, "description": descriptions}
#     return total 

# print(track_spending("food", 10,20,30))
# print(track_spending("travel", 100, tax_rate=0.1))
# print(track_spending("cloths", 50, tax_rate=0.2, description="shoes"))
# print(track_spending("food", 10, description=10))  

# #Higher order functions
# def apply_operations(numbers, operation):
#     return[operation(n) for n in numbers]

# def double(x):
#    return  x * 2

# #using the higher order function
# numbers = [1,2,3]
# result = apply_operations(numbers, double)
# result = apply_operations(numbers , lambda x: x * 2)
# print(result)
# print(result)

# def process_expenses(category, *amounts, operation):
#     if not isinstance(category, str):
#         return "Error: all inputs must be string"
#     if not all(isinstance(amount, (int, float)) for amount in amounts):
#         return "Error: all values must be numeric"
#     processed = [operation(amount) for amount in amounts]
#     return {"category": category, "amounts": processed}

# def add_tax(amount):
#     return amount * 1.1

# print(process_expenses("food",10,20,operation=add_tax))
# print(process_expenses("travel",50,100,operation=lambda x: x * 0.9))
# print(process_expenses(123,10,operation=add_tax))

#Decorator functions:-
# def log_call(func):
#     def wrapper(*args, **kwargs):
#         print(f"calling {func.__name__} with args={args},kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} returned {result}")
#         return result
#     return wrapper

# @log_call
# def add_numbers(a,b):
#     return a + b

# print(add_numbers(3,4))

# def validate_input(func):
#     def wrapper(*args, **kwargs):
#         if not all(isinstance (arg, (int, float))for arg in args):
#             return "Error: all values must be numeric"
#         return func(*args, **kwargs)
#     return wrapper

# @validate_input
# def calculate_total(*amounts, tax_rate=0):
#     total = sum(amounts)
#     return total * (1 + tax_rate)

# print(calculate_total(10,20,30))
# print(calculate_total(10,20,tax_rate=0.2))
# print(calculate_total(10, "20"))
