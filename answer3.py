############################dictionary#################3
"""Write a Python script to add a key to a dictionary. 
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}"""
dictionary={
    0:10,
    1:20
}
dictionary[2]=30
print(dictionary)


""" Write a Python script to concatenate following dictionaries to create a new one. 
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

dict1={
    1:10,
    2:20
}
dict1.update({3:30,4:40})
dict1.update({5:50,6:60})
print(dict1)


""" Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"""
n=int(input())
d=dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)


""" Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. 
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}"""

d={x:x*x for x in range(1,16)}
print(d)


"""Write a Python program to combine two dictionary adding values for common keys. 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})"""

from collections import Counter
import collections
from typing import Collection
dict1={'a': 100, 'b': 200, 'c':300}
dict2= {'a': 300, 'b': 200, 'd':400}
cdict=Counter(dict1)+Counter(dict2)
print(cdict)

"""Write a Python program to print all unique values in a dictionary. 
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}"""

out_dict=[]
input=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
for i in input:
    for j in i:
        if i[j] not in out_dict:
            out_dict.append(i[j])
print(out_dict)

"""Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd"""
List=[]
out_list=[]
input_data={'1':['a','b'], '2':['c','d']}
for i in input_data:
    for j in input_data[i]:
        List.append(j)
out_list.append(List[0]+List[2])
out_list.append(List[0]+List[3])
out_list.append(List[1]+List[2])
out_list.append(List[1]+List[3])
for i in out_list:
    print(i)

"""Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}"""

my_string='w3resource'
my_dict={}
for letter in my_string:
    my_dict[letter]=my_dict.get(letter,0)+1
print(my_dict)

"""Write a Python program to print a dictionary in table format"""
#first_answer
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)
#second_answer
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for key, value in sorted(my_dict.items()):
    print(key,end=" ")
print(end='\n')
for i in my_dict:
    for j in my_dict[i]:
        print(j,end=" ")
        if(j==3 or j==7):
            print(end="\n")
print(end='\n')
    
"""Write a Python program to get the top three items in a shop. 
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item3 45.5
item2 41.3"""

List=[]
my_dict ={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for i in my_dict:
    List.append(my_dict[i])
List.sort()
print("item4",List[-1])
print("item3",List[-2])
print("item2",List[-3])


"""Write a Python program to sort Counter by value. 
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]"""

from collections import Counter
my_dict={'Math':81, 'Physics':83, 'Chemistry':87}
print(Counter(my_dict).most_common(3))


"""Write a Python program to create a dictionary from two lists without losing duplicate values. 
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})"""

from collections import defaultdict
List1=['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
List2=[1, 2, 2, 3]
d=defaultdict(set)
for i,j in zip(List1,List2):
    d[i].add(j)
print(d)


"""Write a Python program to replace dictionary values with their averagestudent_details= 
[
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]"""
student=[
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]




##########################tuple#############################

"""Write a Python program to print a tuple with string formatting. 
Sample tuple : (100, 200, 300)
Output : This is a tuple (100, 200, 300)"""

my_tuple=(100,200,300)
print("This is a tuple",my_tuple)

"""Write a Python program to replace last value of tuples in a list. 
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""
out_list=[]
my_list=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in my_list:
   x=list(i)
   x[-1]=100
   y=tuple(x)
   out_list.append(y)
print(out_list)


"""Write a Python program to remove an empty tuple(s) from a list of tuples. 
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']"""

my_list=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
for i in my_list:
    if len(i)==0:
        my_list.remove(i)
    else:
        pass
print(my_list)

"""Write a Python program to sort a tuple by its float element. 
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]"""

my_list=[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
for i in my_list:




 """Write a Python program to count the elements in a list until an element is a tuple.""" 
num = [10,20,30,(10,20),40]
ctr = 0
for n in num:
    if isinstance(n, tuple):
        break
    ctr += 1
print(ctr)

    

    
"""Write a Python program to count the elements in a list until an element is a tuple.""" 
#isinstance method
num = [10,20,30,(10,20),40]
ctr = 0
for n in num:
    if isinstance(n, tuple):
        break
    ctr += 1
print(ctr)


"""Write a Python program convert a given string list to a tuple. 
Original string: python 3.0
<class 'str'>
Convert the said string to a tuple:
('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
<class 'tuple'>"""
my_list=[]
my_string="python 3.0"
for i in my_string:
    my_list.append(i)
x=tuple(my_list)
print(x)




"""Write a Python program calculate the product, multiplying all the numbers of a given tuple. 
Original Tuple:
(4, 3, 2, 2, -1, 18)
Product - multiplying all the numbers of the said tuple: -864
Original Tuple:
(2, 4, 8, 8, 3, 2, 9)
Product - multiplying all the numbers of the said tuple: 27648"""
def product(original_tuple):


    x=list(original_tuple)
    y=1
    for i in x:
        y=y*i
    return y
print(product((4, 3, 2, 2, -1, 18)))



"""Write a Python program to calculate the average value of the numbers in a given tuple of tuples. 
Original Tuple:
((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Average value of the numbers of the said tuple of tuples:
[30.5, 34.25, 27.0, 23.25]
Original Tuple:
((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
Average value of the numbers of the said tuple of tuples:
[25.5, -18.0, 3.75]"""

def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result

nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print ("Original Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))

nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print ("\nOriginal Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))




"""Write a Python program to convert a tuple of string values to a tuple of integer values. 
Original tuple values:
(('333', '33'), ('1416', '55'))
New tuple values:
((333, 33), (1416, 55))"""


def tuple_int_str(tuple_str):
    result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
    return result
     
tuple_str =  (('333', '33'), ('1416', '55'))
print(tuple_int_str(tuple_str))

"""Write a Python program to convert a given tuple of positive integers into an integer. 
Original tuple:
(1, 2, 3)
Convert the said tuple of positive integers into an integer:
123
Original tuple:
(10, 20, 40, 5, 70)
Convert the said tuple of positive integers into an integer:
102040570"""

def tuple_int_str(tuple_str):
    result=[]
    string=" "
    y=list(tuple_str)
    for x in y:
        result.append(x)
    return ''.join(map(str, result))
     
tuple_str =  (10, 20, 40, 5, 70)
print(tuple_int_str(tuple_str))


""" Write a Python program to check if a specified element presents in a tuple of tuples. 
Original list:
(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
Check if White presenet in said tuple of tuples!
True
Check if Olive presenet in said tuple of tuples!
False"""


my_tuple=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
List=[]
for i in my_tuple:
    for j in i:
        List.append(j)
if 'White' in List:
    print('True')
else:
    print('False')


"""Write a Python program to compute element-wise sum of given tuples. 
Original lists:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Element-wise sum of the said tuples:
(6, 9, 8, 6)
"""

tuple1=(1, 2, 3, 4)
tuple2=(3, 5, 2, 1)
tuple3=(2, 2, 3, 1)
#map(function,iterable)
result=tuple(map(sum,zip(tuple1,tuple2,tuple3)))
print(result)



"""Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples. 
Original list of tuples:
[(1, 2), (2, 3), (3, 4)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[3, 5, 7]
Original list of tuples:
[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[9, -1, 7, 8]"""



List1=[(1, 2), (2, 3), (3, 4)]
new_list=[]
for i in List1:
    x=list(i)
    y=sum(i)
    new_list.append(y)
print(new_list)


"""Write a Python program to convert a given list of tuples to a list of lists. 
Original list of tuples: [(1, 2), (2, 3), (3, 4)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
"""
List=[(1, 2), (2, 3), (3, 4)]
new_list=[]
for i in List:
    x=list(i)
    new_list.append(x)
print(new_list)

List=[(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
new_list=[]
for i in List:
    x=list(i)
    new_list.append(x)
print(new_list)









            



