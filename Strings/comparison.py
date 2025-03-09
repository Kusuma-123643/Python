#Comparing strings  
s1 = input()
s2 = input()
equal = True
if len(s1) != len(s2):
    equal = False
else:
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            equal = False
            break
print("Strings are equal:", equal)