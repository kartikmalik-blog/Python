import math 

def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "invalid operation:"
    
def power(a,b):
    return a ** b
def modulus(a,b):
    return a % b
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        return "cannot return the square root of negative number:"