#Print gender (Male/Female) program according to given M/F using switch
gender=input()
match gender:
    case 'M':
        print("Male")
    case 'F':
        print("Female")
    case _:
        print("Invalid Input")