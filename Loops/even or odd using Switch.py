# Program to check whether a number is EVEN or ODD using switch
n=int(input())
match n%2:
    case 0:
        print("Even")
    case 1:
        print("Odd")