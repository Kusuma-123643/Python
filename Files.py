# 1. Read text file
with open("example.txt", "r") as file:
    print(file.read())

# 2. Write text to .txt file
with open("output.txt", "w") as file:
    file.write("Writing to file using InputStream equivalent in Python")

# 3. Read a file stream
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# 4. Read a file stream with random access
with open("example.txt", "r") as file:
    file.seek(10)  
    print(file.read())

# 5. Read a file from a particular index using seek()
with open("example.txt", "r") as file:
    file.seek(5)
    print(file.read(10))  

# 6. Check file read and write permissions
import os
file_path = "example.txt"
print("Read Access:", os.access(file_path, os.R_OK))
print("Write Access:", os.access(file_path, os.W_OK))