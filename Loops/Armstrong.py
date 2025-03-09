# 8. Write a program to find Armstrong number or not
num = 153
temp = num
sum_of_digits = 0
while temp > 0:
    remainder = temp % 10
    sum_of_digits += remainder ** 3
    temp //= 10

if sum_of_digits == num:
    print("Armstrong Number: True")
else:
    print("Armstrong Number: False")