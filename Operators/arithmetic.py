# 1. Write a function for arithmetic operators (+, -, *, /)
def arithmetic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Division by zero error"
    return addition, subtraction, multiplication, division

a, b = 10, 5
add, sub, mul, div = arithmetic_operations(a, b)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
