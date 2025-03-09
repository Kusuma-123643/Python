# Write a function to get the difference of largest and smallest value 
arr=list(map(int, input().split()))
min_value=arr[0]
max_value=arr[0]
for i in arr:
    if i<min_value:
        min_value=i
    if i>max_value:
        max_value=i
print("Difference:", max_value - min_value)