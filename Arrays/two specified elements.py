# Write a method to verify if the array contains two specified elements(12,23)
arr = list(map(int, input().split()))
f_12 = False
f_23 = False
for n in arr:
    if n==12:
        f_12=True
    if n==23:
        f_23=True
print("Contains 12 and 23:", f_12 and f_23)