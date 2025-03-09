class A:
    def override_method(self): print("Overridden in A")

class B(A):
    def override_method(self): print("Overridden in B")

class C(B):
    def override_method(self): print("Overridden in C")

objA, objB, objC = A(), B(), C()
objA.override_method(), objB.override_method(), objC.override_method()

refA = B()
refA.override_method()

refA = C()
refA.override_method()