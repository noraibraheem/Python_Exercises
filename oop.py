#oop:object oriented programming 
#oop is code styling and paradigm
#paradigm includes attributes and methods where attributes are all information about object but methods are all actions
#oop is multi paradigm programming language is parcedual and oop functional
#precedual is a set of steps to  make task
#functional is a concept of mathematical functions

#################################################

#class is the blueprint or constructor of object
#class instantiate means create instance of class
#class is a key word of class
#class may contains methods and attributes
#__init__ method called every time you create object from class
#__ init__ method is initialze the date for thus object
# self can be named anything
#self refers to current instance
#in python you don't need to call new() to create object


"""class member:
    def __init__ (self):
        print("a new member is added")


member()
member()"""

##########################################################
#self:points to instance created  from class
#instance attributes are defined inside constructor
#instance methods can have more than one parameter like any functionn


"""class student:
    def __init__ (self):
        student.name="osama"

onestudent=student()
print(onestudent.name)"""


"""class student:
    def __init__ (self,fname,mname,lname,gender):
        student.first_name=fname
        student.middle_name=mname
        student.last_name=lname
        student.gender=gender
    def name_with_title(self):
        if self.gender=="male":
            return f"hello mr {self.first_name}"
        else:
            return f"hello miss {self.first_name}"
    def full_name(self):
        return f"hello{self.gender()}{self.first_name}{self.middle_name}{self.last_name}"
    
one_student=student("ahmed","ali","mohamed","male")

print(one_student.first_name,one_student.middle_name,one_student.last_name)
second_student=student("ahmed","mohamed","elhanafy","male")
print(second_student.first_name,second_student.middle_name,second_student.last_name)
print(one_student.name_with_title())
print(second_student.full_name())"""

##########################################################################################
#class attributes defined outside constructor
#class method:
#marked with @classmethod decorator to flag to it as class method
#it takes cls as argument not self to pointts to the class not instance argument
#static methods:1.it takes no parameters
#2.its bound to the class not instance
#3.used when doing something doesn't have acces to object or class

    

     

    

        
