# 1. Program to generate Arithmetic Exception without exception handling
print(10 / 0)  # This will cause ZeroDivisionError

# 2. Handle the Arithmetic exception using try-except block
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# 3. Write a method which throws an exception, Call that method in main class without try block
def throw_exception():
    raise ValueError("This is a ValueError")

throw_exception()  # This will stop the program

# 4. Program with multiple except blocks
try:
    x = int("abc")
except ValueError:
    print("Value Error Occurred")
except ZeroDivisionError:
    print("Zero Division Error Occurred")

# 5. Program to throw an exception with a custom message
def check_number(n):
    if n < 0:
        raise Exception("Negative numbers not allowed")
    print("Number is valid")

check_number(-5)

# 6. Program to create your own exception
class MyException(Exception):
    def __init__(self, message):
        self.message = message

raise MyException("This is my custom exception")

# 7. Program with finally block
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
finally:
    print("This will always execute")

# 8. Program to generate Arithmetic Exception
print(10 / 0)

# 9. Program to generate FileNotFoundError
open("non_existent_file.txt", "r")

# 10. Program to generate ModuleNotFoundError (ClassNotFoundException equivalent)
import non_existent_module

# 11. Program to generate IOError (Handled using OSError in Python)
raise OSError("This is an IO Exception")

# 12. Program to generate AttributeError (NoSuchFieldException equivalent)
class Example:
    pass

obj = Example()
print(obj.non_existent_field)