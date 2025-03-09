from abc import ABC, abstractmethod

# 1. Abstract class with abstract and non-abstract methods
class AbstractClass(ABC):
    def non_abstract_method(self):
        return "Non-Abstract Method in AbstractClass"

    @abstractmethod
    def abstract_method(self):
        pass

# 2. Subclass for abstract class
class ChildClass(AbstractClass):
    def abstract_method(self):
        return "Abstract Method Implemented in ChildClass"

    def call_abstract_method(self):
        return self.abstract_method()

    def call_non_abstract_method(self):
        return self.non_abstract_method()

# 3 & 4. Creating instances and calling methods
child_obj = ChildClass()
print(child_obj.call_abstract_method())  # Calling abstract method
print(child_obj.call_non_abstract_method())  # Calling non-abstract method