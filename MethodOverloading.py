# 1 & 2. Method Overloading using default arguments
class MethodOverloading:
    def add(self, a, b=0):
        print("Sum:", a + b)

    def add_different_types(self, a, b=None):
        if b is None:
            print("Single Parameter:", a)
        else:
            print("Different Data Types:", str(a) + str(b))

obj = MethodOverloading()
obj.add(5)          
obj.add(5, 10)      
obj.add_different_types(5)      
obj.add_different_types(5, "Hello")  

# 3. Two methods with the same name and same number of parameters (Not possible in Python)
class SameMethod:
    def show(self, a):
        print("Method 1:", a)

    def show(self, a):  
        print("Method 2:", a)

obj2 = SameMethod()
obj2.show(10)  # Calls the latest defined method