#Matching a String Against a Regular Expression With matches() 
import re
pattern = r"Hello"
text = "Hello, world!"
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")