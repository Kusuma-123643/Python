# 1. Write a program to print your name.
print("Kuppili Kusuma")

# 2. Write a program for a Single line comment and multi-line comments

# This is a single-line comment

"""
This is a multi-line comment.
"""

# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

int_var = 10
bool_var = True
char_var = 'A'
float_var = 10.5
double_var = 20.123456789

print("Integer:", int_var)
print("Boolean:", bool_var)
print("Character:", char_var)
print("Float:", float_var)
print("Double (Float in Python):", double_var)

# 4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables.

global_var = "I am a global variable"

def scope_example():
    global_var = "I am a local variable"
    print("Inside function:", global_var)

scope_example()
print("Outside function:", global_var)