#Write a function to remove a specific element from an array 
def remove(l,n):
    return [x for x in l if x!=n]

l = list(map(int, input().split()))
n = int(input())
print(remove(l, n))