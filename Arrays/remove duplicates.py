# Write a method to remove duplicate elements from an array
arr = list(map(int, input().split()))
unique = []
d=[]
for num in arr:
    if num not in unique:
        unique.append(num)
    else:
        d.append(num)
print("Duplicates: ", d)
print("Array without Duplicates:", unique)