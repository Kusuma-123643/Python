#Write a function to calculate the average value of an array of integers
def avgOfArray(arr):
    return sum(arr)/len(arr)
arr=list(map(int,input().split()))
print(avgOfArray(arr))
