############################lambda function####################33
#lambda argument:expressions

"""Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number. 
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75"""


x=lambda arg:arg*3
print(x(15))



"""Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]"""

List=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
result=sorted(List,key=lambda x:x[1])
print(result)


"""Write a Python program to sort a list of dictionaries using Lambda. 
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]"""
List=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
result=sorted(List,key=lambda x:x['color'])
print(result)

"""Write a Python program to filter a list of integers using Lambda. 
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]"""
List=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#using filter to return boolean result >>>filter(func,iterable)
even_elements=filter(lambda x:x%2==0,List)
print(list(even_elements))
odd_elements=filter(lambda x:x%2!=0,List)
print(list(odd_elements))

"""Write a Python program to square and cube every number in a given list of integers using Lambda. 
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]"""

my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_list=map(lambda x:x**2,my_list)
print(list(square_list))

cube_list=map(lambda x:x**3,my_list)
print(list(cube_list))


"""Write a Python program to find if a given string starts with a given character using Lambda. 
Sample Output:
True
False"""

result=lambda my_string: True if my_string.startswith('p') else False
print(result('python'))





"""Write a Python program to extract year, month, date and time using Lambda. 
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178"""
import datetime
from typing import Counter
x=datetime.datetime.now()
print(x)
year=lambda x:x.year
print(year(x))
month=lambda x:x.month
print(month(x))
day=lambda x:x.day
print(day(x))







"""Write a Python program to check whether a given string is number or not using Lambda. 
Sample Output:
True
True
False
True
False
True
Print checking numbers:
True
True
"""



check=lambda x: True if type(x)==int else False
print(check("nora"))
print(check(33))

"""how to add two lists(map function)"""
my_list1=[1,2,3,4,5,6,7]
my_list2=[1,2,3,4,5,6,7]
addition=map(lambda x,y:x+y , my_list1,my_list2)
print(list(addition))

"""fiter function gives us a boolean result"""


from functools import reduce
my_list=[1,2,3,4,5]
result=reduce(lambda x,y:x+y,my_list)
print(result)

"""Write a Python program to rearrange positive and negative numbers in a given array using Lambda. Go to the editor
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]"""

my_list=[-1, 2, -3, 5, 7, 8, 9, -10]
result=sorted(my_list,key=lambda x: 0 if x==0 else -1/x)
print(list(result))



""" Write a Python program to count the even, odd numbers in a given array of integers using Lambda. Go to the editor
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5"""


my_list=[1, 2, 3, 5, 7, 8, 9, 10]
even_counter=len(list(filter(lambda x: x%2==0,my_list)))
odd_counter=len(list(filter(lambda x: x%2!=0,my_list)))
print("Number of even numbers in the above array ",even_counter)
print("Number of odd numbers in the above array ",odd_counter)

def even_odd(List):
    even=0
    odd=0
    for i in List:
        if i%2==0:
            even+=1
        else:
            odd+=1
    print(f"Number of even numbers in the above array:{even}")
    print(f"Number of odd numbers in the above array:{odd}")

even_odd([1, 2, 3, 5, 7, 8, 9, 10])



"""Write a Python program to find the values of length six in a given list using Lambda.
Sample Output:
Monday
Friday
Sunday"""
my_list=["saturday","sunday","monday","tuesday","wendsday","thursday","friday"]
result=list(filter(lambda x: len(x)==6,my_list))
for day in result:
    print(day)


""" Write a Python program to add two given lists using map and lambda. Go to the editor
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]"""

list1=[1,2,3]
list2=[4,5,6]
result=list(map(lambda x,y:x+y,list1,list2))
print(result)


"""Write a Python program to find the second lowest grade of any student(s) from the given names and grades of each student using lists and lambda. Input number of students, names and grades of each student. Go to the editor
Input number of students: 5
Names and Grades of all students:
[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
Second lowest grade: 2.0
Names:
N KAR"""

students=[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
result= sorted(students,key=lambda x: x[1] )
numbers=[]
for i in result:
    for j in i:
        if isinstance(j,float):
            numbers.append(j)
        else:
            pass
print(numbers[-2])



""" Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda. 
Orginal list:
[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
Numbers of the above list divisible by nineteen or thirteen:
[19, 57, 39, 152, 190]"""

my_list=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
result=filter(lambda x: x%19==0 or x%30==0,my_list)
print(list(result))



"""Write a Python program to find palindromes in a given list of strings using Lambda. Go to the editor
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']"""
# palindromes:that remains the same when its digits are reversed
#filter>>>boolean result/conditions
my_list=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
palindromes=list(filter(lambda x:x=="".join(reversed(x)),my_list))
print(palindromes)


"""Write a Python program to find all anagrams of a string in a given list of strings using lambda. Go to the editor
Orginal list of strings:
['bcda', 'abce', 'cbda', 'cbea', 'adcb']
Anagrams of 'abcd' in the above string:
['bcda', 'cbda', 'adcb']"""
from collections import Counter
my_list=['bcda', 'abce', 'cbda', 'cbea', 'adcb']
string='abcd'
#we will use counter function it calculates number o repeated elements in iterable
result=list(filter(lambda x:Counter(string)==Counter(x) ,my_list))
print(result)

"""Write a Python program to find the numbers of a given string and store them in a list,
 display the numbers which are bigger than the length of the list in sorted form. Use lambda function to solve the problem. Go to the editor
Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
Numbers in sorted form:
20 23 56"""

string=" sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
my_list=string.split()
print(my_list)   
#isdigit returns true if all digits in string is true else rturn false
numbers=sorted([int(x) for x in my_list if x.isdigit()])
print(numbers)
for i in filter(lambda x:x>len(numbers),numbers):
    print(i,end=" ")
print('\n')


"""Write a Python program that multiply each number of given list with a given number using lambda function. Print the result.
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22"""
my_list=[2, 4, 6, 9, 11]
y=int(input())
for i in list(map(lambda x:y*x,my_list)):
    print(i,end=" ")


"""Write a Python program that sum the length of the names of a given list of names after removing the names that starts with an lowercase letter.
 Use lambda function. 
Result:"""
sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
print("Result:")
#convert list into string to calculate the length of all characters together
print(len(''.join(sample_names)))



"""Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function. 
Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
Sum of the positive numbers: -32
Sum of the negative numbers: 48"""

from functools import reduce
List=[2, 4, -6, -9, 11, -12, 14, -5, 17]
pos=[]
for i in List:
    if i>0:
        pos.append(i)
print(pos)
sum_positive=reduce(lambda x,y:x+y ,pos)
negative=[]
for i in List:
    if i<0:
        negative.append(i)
sum_negative=reduce(lambda x,y: x+y,negative)
print("Sum of the positive numbers:",sum_positive)
print("Sum of the negative numbers:",sum_negative)


"""Write a Python program to find numbers within a given range where every number is divisible by every digit it contains. 
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]"""




"""Write a Python program to create the next bigger number by rearranging the digits of a given number. 
Original number: 12
Next bigger number: 21
Original number: 10
Next bigger number: False
Original number: 201
Next bigger number: 210
Original number: 102
Next bigger number: 120
Original number: 445
Next bigger number: 454"""

number=int(input("oruginal number: "))
result=lambda x:x
