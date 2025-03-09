#Write a function to reverse an array of integer values
arr = list(map(int, input().split()))
reversed_arr = []
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])
print("Reversed Array:", reversed_arr)