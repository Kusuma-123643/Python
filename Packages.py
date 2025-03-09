class Class1:
    def __init__(self):
        print("Class1 Constructor")

    def method1(self):
        return "Method of Class1"

class Class2:
    def __init__(self):
        print("Class2 Constructor")

    def method2(self):
        return "Method of Class2"

obj1 = Class1()
print(obj1.method1())

obj2 = Class2()
print(obj2.method2())