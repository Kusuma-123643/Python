#Converting to uppercase and lowercase
s = input()
uppercase = ''
lowercase = ''
for char in s:
    if 'a' <= char <= 'z':
        uppercase += chr(ord(char) - 32)
        lowercase += char
    elif 'A' <= char <= 'Z':
        lowercase += chr(ord(char) + 32)
        uppercase += char
    else:
        uppercase += char
        lowercase += char
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)