#Converting integer objects to Strings 
n = int(input())
digits = []
while n > 0:
    digits.append(chr((n% 10) + 48))
    n //= 10
string_num = ''
for i in range(len(digits) - 1, -1, -1):
    string_num += digits[i]

print("Converted String:", string_num)