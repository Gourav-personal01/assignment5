#The Method which Outputs the Value which we are looking for on the basis of Input is called getter Method.
# The Method Which Changes the Value which we want to change and Outputs the New Result is called setter method.

#Example - 

class age_of_student:
    def __init__(self,age):
        self.age = age

    def get_age_of_student(self):
        return self.age
    
    def set_age_of_student(self,new_age):
        if new_age>= self.age:
            self.age = new_age
            return self.age
obj = age_of_student(5)
print(obj.get_age_of_student())
print(obj.set_age_of_student(18))
print(obj.get_age_of_student())