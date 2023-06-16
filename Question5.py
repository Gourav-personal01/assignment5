# Method Overiding is the Method Which Gives an option to sub class to change some sort of method of their superclass with the help of inherit option.

#Example - 

class super_class:
    def __init__(self):
        self.value = "Hi This is a parent Class"
    
class sub_class(super_class):
    def __init__(self):
        self.value = "Hi This is Child class"

obj1 = super_class()
obj2 = sub_class()
print(obj1.value)
print(obj2.value)