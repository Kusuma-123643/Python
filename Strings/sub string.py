#Extract a string using Substring
s = input()
start = int(input())
end = int(input())
substring = ''
for i in range(start, end):
    substring += s[i]
print("Substring:", substring)