 #oop is organizd first 1960
 #it is organized to use/understand/maintain and extend
 #oop has three pillars are(encapsulation/inheritance/polymoriphism)
 #every thing is object
 #object is a copy of class --لما اجي اخد اوبجيكت من كلاس اسم الاوبجكت ده بينباصى لل كلاس ك ارجيومينت
 #so we use self as a default argument to point to current instance فيفهم لما اباصيلها اسم الابوجيكت ومطلعش ايرورز
 #self is a placeholder o object
 #constructor is an usual method but it is excuted firstly def__init__()
 


class student:
    age=34 #atrribute 
    def __init__ (self,name):
        self.name=name 
        
        print(f"hello {name}")

onestudent=student("ahmed")
print("#"*10)
onestudent=student("ali")
onestudent.age=55
print(onestudent.age)
z=student("hanafy")
print(z.age)
z.age=88
del z.age
print(z.age)



class employee:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        self.marks=[]
        print(f"hello mr {name} your age is {age}")
    def sum_marks(self,mark):
        self.marks.append(mark)
    def average_marks(self):
        return sum(self.marks)/len(self.marks)


x=employee("ahmed",23)
x.sum_marks(10)
x.sum_marks(30)
x.sum_marks(20)
print(x.average_marks())


#---------------------------------------------<calculator_example>---------------------------------#

class calculator:
    def __init__ (self,a,b):  #constructor
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b

x=calculator(20,30)
print(x.add())
print(x.mul())
############################
#############################
################################
#inherience:inherint attributes and methods(عشان الكود ميطولش مدام نفس الحاجه موجوده ف كلاس تاني فانا بورثها وخلاصwها وخلاص)
#inheriting class is called child class/derived class/subclass
#an inherited class is called parent class/super class/base class

#POLYMORIPHISM that classes have the same methods but each method make different task


#super inherience:
#super used to relate the classs with its parent class
#If the class doesn't have __init__ constructor python will check its parent class
#we use super() function to call methods in the parent class

class animal:
    def __init__ (self,name):
        self.name=name
class dog(animal):
    """def __init__ (self,name):
        super(dog,self).__init__(name)
        self.food='fish'"""
    def foods(self,food):
        self.food=food
        return f"{self.name} eats {self.food}"
    def fetch(self,thing):
        print("%s goes after %s"%(self.name,thing))
d=dog("misho")
print(d.name)
print(d.foods("rice"))




