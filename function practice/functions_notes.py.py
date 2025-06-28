# Python Functions Summary
# A compilation of all function concepts covered, with examples and explanations.
# Topics: Basics, Return, Default Parameters, Mutable Defaults, Scope, *args/**kwargs, Higher-Order Functions, Lambdas, Decorators

# 1. Function Basics and Return Statements
# Functions are defined with 'def', take parameters, and use 'return' to output values. Without 'return', they return None.
def add_numbers(a, b):
    return a + b

# Example usage
print(add_numbers(3, 4))  # Output: 7
print(add_numbers(-1, 5))  # Output: 4
# Without return, print(add_numbers(3, 4)) would output None

# 2. Default Parameters and Keyword Arguments
# Default parameters make arguments optional. Keyword arguments improve readability.
def calculate_total(price, quantity, discount=0):
    if not (isinstance(price, (int, float)) and isinstance(quantity, (int, float)) and isinstance(discount, (int, float))):
        return "Error: All inputs must be numbers"
    return price * quantity * (1 - discount)

# Example usage
print(calculate_total(10, 2))  # Output: 20.0 (no discount)
print(calculate_total(10, 2, 0.1))  # Output: 18.0 (10% discount)
print(calculate_total(price=10, quantity=2, discount=0.2))  # Output: 16.0 (keyword args)

# 3. Mutable Default Parameters
# Avoid mutable defaults (e.g., lists) as they persist across calls. Use None instead.
def add_to_cart(item, cart=None):
    if not isinstance(item, str):
        return "Error: Item must be a string"
    if cart is None:
        cart = []
    cart.append(item)
    return cart

# Example usage
print(add_to_cart("apple"))  # Output: ["apple"]
print(add_to_cart("banana"))  # Output: ["banana"]
print(add_to_cart("apple", ["milk"]))  # Output: ["milk", "apple"]
print(add_to_cart(123))  # Output: "Error: Item must be a string"

# Bad practice example (mutable default)
def bad_cart(item, cart=[]):
    cart.append(item)
    return cart

print(bad_cart(1))  # Output: [1]
print(bad_cart(2))  # Output: [1, 2] (shared list persists)

# 4. Variable Scope
# Local variables are confined to the function. Global variables require 'global' to modify (avoid when possible).
total_sales = 0

def record_sales(product, *quantities, discount_rate=0):
    if not isinstance(product, str):
        return "Error: Product must be a string"
    if not all(isinstance(qty, (int, float)) for qty in quantities):
        return "Error: All quantities must be numbers"
    price_per_unit = 50  # Local variable
    total = sum(quantities) * price_per_unit * (1 - discount_rate)
    return total

# Example usage
print(record_sales("laptop", 2, 3))  # Output: 250.0
print(record_sales("phone", 1, discount_rate=0.2))  # Output: 40.0
print(record_sales(123, 2))  # Output: "Error: Product must be a string"

# Global variable example (avoid)
def update_global_sales(product, *quantities, discount_rate=0):
    global total_sales
    if not isinstance(product, str):
        return "Error: Product must be a string"
    if not all(isinstance(qty, (int, float)) for qty in quantities):
        return "Error: All quantities must be numbers"
    price_per_unit = 50
    total = sum(quantities) * price_per_unit * (1 - discount_rate)
    total_sales += total
    return total

# 5. *args and **kwargs
# *args collects variable positional arguments into a tuple. **kwargs collects keyword arguments into a dictionary.
def track_spending(category, *amounts, **options):
    if not isinstance(category, str):
        return "Error: Category must be a string"
    if not all(isinstance(amount, (int, float)) for amount in amounts):
        return "Error: All amounts must be numbers"
    description = options.get("description")
    if description is not None and not isinstance(description, str):
        return "Error: Description must be a string"
    total = sum(amounts)
    if options.get("tax_rate"):
        total *= (1 + options["tax_rate"])
    if description:
        return {"category": category, "total": total, "description": description}
    return total

# Example usage
print(track_spending("food", 10, 20, 30))  # Output: 60.0
print(track_spending("travel", 100, tax_rate=0.1))  # Output: 110.0
print(track_spending("clothes", 50, tax_rate=0.2, description="new shoes"))  # Output: {"category": "clothes", "total": 60.0, "description": "new shoes"}
print(track_spending("food", 10, description=123))  # Output: "Error: Description must be a string"

# 6. Higher-Order Functions and Lambda Functions
# Higher-order functions take functions as arguments. Lambdas are concise, one-line functions.
def process_expenses(category, *amounts, operation):
    if not isinstance(category, str):
        return "Error: Category must be a string"
    if not all(isinstance(amount, (int, float)) for amount in amounts):
        return "Error: All amounts must be numbers"
    processed = [operation(amount) for amount in amounts]
    return {"category": category, "amounts": processed}

def add_tax(amount):
    return amount * 1.1

# Example usage
print(process_expenses("food", 10, 20, operation=add_tax))  # Output: {"category": "food

# 7. Decorators
# Decorators wrap functions to add functionality (e.g., logging, validation) without modifying the original code.
def validate_inputs(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args):
            return "Error: All inputs must be numbers"
        return func(*args, **kwargs)
    return wrapper

@validate_inputs
def calculate_total(*amounts, tax_rate=0):
    total = sum(amounts)
    return total * (1 + tax_rate)

# Example usage
print(calculate_total(10, 20, 30))  # Output: 60.0
print(calculate_total(10, 20, tax_rate=0.1))  # Output: 33.0
print(calculate_total(10, "20"))  # Output: "Error: All inputs must be numbers"

# Decorator for logging
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_call
def add_numbers(a, b):
    return a + b

# Example usage
print(add_numbers(3, 4))  # Output: Calling add_numbers with args=(3, 4), kwargs={}
#                   add_numbers returned 7
#                   7