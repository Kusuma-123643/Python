# 3. Write a program to find the index of an array element
def find_index(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1
arr={1, 5, 6,24, 65}
print("Index of 3:", find_index(arr, 3))
