# Write a program to find the common values between two arrays
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
common = []
for i in arr1:
    for j in arr2:
        if i == j and i not in common:
            common.append(i)
print("Common Values:", common if common else "No Common Values")