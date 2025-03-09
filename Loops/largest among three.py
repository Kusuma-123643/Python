# 5. Write a program to print largest number among three numbers.
a, b, c = 10, 25, 15
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

print("Largest Number:", largest)