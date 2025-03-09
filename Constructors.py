# 1. Class with multiple constructors
class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor")
        elif arg2 is None:
            print("One Argument Constructor:", arg1)
        else:
            print("Two Argument Constructor:", arg1, arg2)

obj1 = MyClass()
obj2 = MyClass(10)
obj3 = MyClass(10, 20)

# 2. Calling super class constructors from child class
class Parent:
    def __init__(self, value=None):
        if value is None:
            print("Parent Default Constructor")
        else:
            print("Parent Argument Constructor:", value)

class Child(Parent):
    def __init__(self, value=None):
        super().__init__(value)
        print("Child Constructor")

child1 = Child()
child2 = Child(50)

# 3. Constructor with access modifiers
class AccessModifiers:
    def __init__(self):  # Public
        print("Public Constructor")
    
    def _protected_init(self):  # Protected
        print("Protected Constructor")
    
    def __private_init(self):  # Private
        print("Private Constructor")

obj = AccessModifiers()
obj._protected_init()

# 4. Attributes of a constructor
class AttributesExample:
    def __init__(self, name):
        self.name = name  # Instance attribute

    def show(self):
        print("Name:", self.name)

obj_attr = AttributesExample("Python")
obj_attr.show()