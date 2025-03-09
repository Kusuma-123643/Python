#Write a program to print the odd and even numbers.
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print("Even Numbers")
for i in e:
    print(i,end=" ")
print()
print("Odd numbers")
for i in o:
    print(i,end=" ")