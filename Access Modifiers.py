# 1. Class with private fields and method
class PrivateClass:
    def __init__(self):
        self.__private_field = "Private Field"

    def __private_method(self):
        return "Private Method Called"

    def access_private_method(self):
        return self.__private_method()

class SubPrivateClass(PrivateClass):
    def access_private_from_subclass(self):
        try:
            return self.__private_field  # Trying to access private field
        except AttributeError:
            return "Cannot access private field from subclass"

obj = PrivateClass()
print(obj.access_private_method())

sub_obj = SubPrivateClass()
print(sub_obj.access_private_from_subclass())

# 2. Class with protected fields and methods
class ProtectedClass:
    def __init__(self):
        self._protected_field = "Protected Field"

    def _protected_method(self):
        return "Protected Method Called"

class SubProtectedClass(ProtectedClass):
    def access_protected_from_subclass(self):
        return self._protected_field, self._protected_method()

obj_protected = ProtectedClass()
print(obj_protected._protected_field, obj_protected._protected_method())

sub_obj_protected = SubProtectedClass()
print(sub_obj_protected.access_protected_from_subclass())

# 3. Class with public fields and methods
class PublicClass:
    def __init__(self):
        self.public_field = "Public Field"

    def public_method(self):
        return "Public Method Called"

obj_public = PublicClass()
print(obj_public.public_field, obj_public.public_method())