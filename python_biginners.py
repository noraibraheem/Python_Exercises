"""#ask the user about its name and fav color
name=input("what's your name? ")
color=input("what's your fav color?")
print(f"{name} like {color}")

#ask the user their weights (in pounds) convert it into kilograms and print on the terminal
weight=input("what's your weights in pounds ?")
weight_kg=int(weight)*1000
print(weight_kg)"""

#string
course="python for beginners"
print(course.lower())
print(course.upper())
print(len(course))
print(course.find('p'))  #returns an index
print(course.replace('p','f'))  #take an charcter of a sequence of characters
print('beginners'in course)  #returns boolean value true/false
print(course.title())    #returns a string but with each word starts with upper character

#precedance in python
#1-exponentiation
#2-multiplication or division
#3-addition or subtraction

#there's some functions which deel with numbers
#first is round()
x=2.9
print(round(x))
print(abs(-2))
#most of mathematical functions are found in math module
import math

print(pow(2,3))
print(math.floor(2.9))  #round the number to the small near value

#if statements build programs that can make decisions which based on some conditions


#AND includes both
#OR includes one at least
#NOT -->negative


###################################################################
"""initial
while condition:
    statement
    increament"""


########## nested loop ##########
for x in range (4):
    for y in range(3):
        print(f"({x},{y})")




numbers=[5,2,5,2,2]
for i in numbers:
    print('x'*i)

#####how to find the largest num of list #########33
List=[10,20,30,40,50]
print(max(List))
max_num=List[0]
for i in List:
    if i>max_num:
        max_num=i
print(max_num)


###two dimensional list 
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for item in row:
        print(item)


################## Methods of loop ##############
#1-APPEND
#2-INSERT (INDEX,ITEM)
#3-CLEAR() clear all items of list
#4-pop() remove the last item of list
#5-index() get th index of definite item
#6-in check if item is ound in list or not---> it returns true or false
#7-sort() vs sorted()
numbers=[7,3,4,8,1,2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
new_list=sorted(numbers).copy()
print(new_list)


########## Write a program to remove the duplicated elements of list #########
List=[1,2,2,7,7,5,6,6,8]
uniques=[]
for number in List:
    if number not in uniques:
        uniques.append(number)
print(uniques)

    
############# tuple a nother structure in python ############
#tuples are immutable we can't change it , modify or remove items

#unpacking in tuples
coordinates=(1,2,3)
x,y,z=coordinates #x is asssigned to first item in tuple ,y is assigned to next item and z is assigned to third item
print(x,y,z)


#example of dictionary
phone=input("phone: ")
digits={
"1":"one",
"2":"two",
"3":"three",
"4":"four"
}
output=" "
for ch in phone:
    output+=digits.get(ch,"!")+" "
print(output)



######################try and exception##########
try:
    age=int(input("enter your age please:"))
    total=20000/age
    print(total)
except ZeroDivisionError:
    print("divided zero isn't allowed")
except ValueError:
    print("enter true type")


# modules are used for organization which derived code into sections
import oop__educated
oop__educated.calculator(20,34)


