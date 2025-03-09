#Write a function to insert an element at a specific position in the array 
arr=list(map(int,input().split()))
p=int(input())
n=int(input())
arr.insert(p,n)
print(arr)