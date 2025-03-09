#Write a function to find the minimum and maximum value of an array
arr = list(map(int, input().split()))
min_value = arr[0]
max_value = arr[0]
for n in arr:
    if n < min_value:
        min_value = n
    if n > max_value:
        max_value = n
print("Min:", min_value, "Max:", max_value)