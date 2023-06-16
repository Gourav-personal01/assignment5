#Suppose we have 2 different Classes with their different properties, if we can use both of the properties in the 3rd Class then it is called as Multiple Inheritance.

#Example 

class class1:
    def func1(self):
        return "This is func 1"
class class2:
    def func2(self):
        return "This is func 2"
class class3(class1,class2):
    def func3(self):
        return "This is func 3"
a = class3()
print(a.func1())
print(a.func2())
print(a.func3())