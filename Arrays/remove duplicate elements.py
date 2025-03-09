#Write a program to remove the duplicate elements and return the new array
arr=list(map(int, input().split()))
unique=[]
for n in arr:
    if n not in unique:
        unique.append(n)
print("Array without Duplicates:", unique)