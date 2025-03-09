# 2. Write a method for increment and decrement operators (++, --)
def increment_decrement(n):
    incremented = n + 1
    decremented = n - 1
    return incremented, decremented

num = 7
inc, dec = increment_decrement(num)
print("Incremented Value:", inc)
print("Decremented Value:", dec)