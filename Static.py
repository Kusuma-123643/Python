class MyClass:
    # Define a static variable
    static_var = 10

# 1. Access static variable through class
print("Access through class:", MyClass.static_var)

# 2. Access static variable through an instance
obj1 = MyClass()
print("Access through instance:", obj1.static_var)

# 3. Change static variable within an instance (creates an instance variable, doesn't modify the class variable)
obj1.static_var = 20
print("Instance changed static_var:", obj1.static_var)  # This affects only obj1
print("Class static_var remains:", MyClass.static_var)  # The class variable remains unchanged

# 4. Change static variable within the class (affects all instances)
MyClass.static_var = 30
print("Class static_var changed:", MyClass.static_var)

# Checking if new instances reflect the class-level change
obj2 = MyClass()
print("New instance sees class change:", obj2.static_var)