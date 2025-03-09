#Write a function to test if array contains a specific value
def contains_value(arr,n):
    return n in arr

arr = list(map(int, input().split()))
n = int(input())
print("Exists:", contains_value(arr, n))