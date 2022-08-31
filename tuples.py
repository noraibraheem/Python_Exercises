# tuples
# tuples are immutable can't be modified
# tuples items aren't unique , used all data types
# allowed operators as lists and strings
# items are ordered have an index
# items are inclosed in ()


from typing import Tuple


x = ("ahmed", "mohammed", "ali")
y = "ahmed", "mohammed", "ali"
print(type(x))
print(type(y))

# tuple with one element
x = ("ahmed",)  # comma(,) is neccessary for difintion tuple wwith one elememt
print(type(x))
y = ("ahmed")
print(type(y))

# concatenation
a = (1, 2, 3, 4)
b = (5, 6)
c = a+b
print(c)

# tuple is repeated by (*)
a = ("osama",)
print(a)
print(a*6)

# count
mytuple = (1, 2, 3, 4, 1, 3, 5, 1)
print(mytuple.count(1))
print(mytuple.count(3))

# tuple destruct
a = ("a", "b", "c")
x, y, z = a
print(x)
print(y)
print(z)

y = (1, 2, 3, 4)
a, b, _, c = y
print(a)
print(b)
print(c)




print(1,000,000 )

"""Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number"""
summ=0
List=[]
try:
    while True:
        num=input("enter plz number")
        if num=="done":
            for i in List:
                summ=summ+i
            average=summ/len(List)
            break
        else:
            List.append(int(num)) 
    print(average , summ ,len(List))
except:
    print("invalid value")