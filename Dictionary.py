# 1.1 Adding values in dictionary
students = {101: "Alice", 102: "Bob", 103: "Charlie", 104: "David", 105: "Eve"}
print(students)

# 1.2 Updating values in dictionary
students[102] = "Brian"
print(students)

# 1.3 Accessing value in dictionary
print(students[103])

# 1.4 Creating a nested dictionary
nested_students = {
    "ClassA": {101: "Alice", 102: "Bob"},
    "ClassB": {103: "Charlie", 104: "David"}
}
print(nested_students)

# 1.5 Access values of nested dictionary
print(nested_students["ClassA"][101])

# 1.6 Print keys in dictionary
print(students.keys())

# 1.7 Delete a value from dictionary
del students[104]
print(students)