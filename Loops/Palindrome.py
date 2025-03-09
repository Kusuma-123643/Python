# 10. Write a program to check palindrome or not.
num = 121
temp = num
reverse_num = 0

while temp > 0:
    remainder = temp % 10
    reverse_num = reverse_num * 10 + remainder
    temp //= 10

if num == reverse_num:
    print("Palindrome: True")
else:
    print("Palindrome: False")