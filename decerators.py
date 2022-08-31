#decerators
#it caled sometimes meta programming
#everything in python is an object even function
#it takes a function and add some functionality then returns it
#wrap other function and enhance behaviour


def mydecerator(func):
    def nested_decerator(): #any name for decoration
        print("before")   #message from decerator
        func()            #EXCUTE FUNCTION
        print("after")      #Mmessage from decerator
    return nested_decerator   #return all data

def say_hello():
    print("hello python")

say_hello()  #calling function without decoration
print("#" * 50)
decerator=mydecerator(say_hello)
decerator()

print("#" * 50)

@mydecerator
def say_hello():
    print("hello python")

say_hello()

print("#" * 100)

#decerator accepts parameters
def my_decerator(func):
    def nested_dec(num1,num2):
        print("sum of two integer numbers")
        func(num1,num2)
    return nested_dec

def mysecond_decerator(func):
    def nested_dec(num1,num2):
        print("coming from second deceator")
        func(num1,num2)
    return nested_dec


@my_decerator
@mysecond_decerator
def calc(n1,n2):
    print(n1+n2)

calc(10,90)


print("#" * 100)

#speed time test

from time import time
def speed_time(func):
    def nested_func():
        start=time()
      
        func()
        end=time()
        print(f"your run time speed is:{end-start}")
    return nested_func

@speed_time
def bigger():
    for i in range(1,1000):
        print(i)

bigger()



