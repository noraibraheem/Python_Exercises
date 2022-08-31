"""Write a Python program to count the number of strings where the string length is 2 or more and the first 
and last character are same from a given list of strings.  Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

List=['abca', 'xyz', 'aba', '1221']
turn=0
for i in range(0,len(List)):
    if len(List[i])>=2 and List[i][0]==List[i][-1]:
        turn+=1
print(turn) 




"""Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.  
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]  ترتيب تصاعدي حسب العنصر الاخير
"""
List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result=sorted(List,key=lambda x:x[1])
print(result)






"""Write a Python program to remove duplicates from a list."""
List=[1,2,3,3,4,5,6]
second_List=[]
for number in List:
    if number not in second_List:
        second_List.append(number)
print(second_List)


"""Write a Python program to check a list is empty or not.  """
List=[]
if len(List)>0:
    print("List is not empty")
else:
    print("List is empty")



"""Write a Python program to find the list of words that are longer than n from a given list of words """
def longest_word(n,List):
    out_List=[]
    for num in range (0,len(List)):
        if len(List[num])>n:
            out_List.append(List[num])
    print(out_List)

longest_word(4,["hello","world","every","one"])


"""Write a Python function that takes two lists and returns True if they have at least one common member """
def comparison (first_list,second_list):
    redult=False
    for i in first_list:
        for j in second_list:
            if i==j:
                result=True
                return result
                
            
print(comparison(["three",2,3,4],[1,2,"three",4]))


"""Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. """
#thus code to remove an element of list in specified position which entered by user
pos=int(input())
def removal_list(List,position):
    if position<len(List):
        List.remove(List[position])
        return List
    else:
        return "list index out of range"

print(removal_list(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],pos))  

#to remove elements in positions 0th,4th,5th
"""List=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for element in range(0,len(List)):
    if element==0 or element==4 or element==5:
        List.remove(List[element])
print(List)
"""

"""Write a Python program to get unique values from a list """

List=[4,5,1,1,2,3,3,4,5,6]
List=set(List)
second_List=[]
for number in List:
    if number not in second_List:
        second_List.append(number)
print(second_List)



    
"""Write a Python program to get the frequency of the elements in a list """

random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
frequency = {}
for item in random_list:
   if item in frequency:
      frequency[item] += 1  #value of key in dict 
   else:
      frequency[item] = 1

print(frequency)


"""Write a Python program to count the number of elements in a list within a specified range"""
List=[1,2,3,4,5,6,7,8]
counter=0
for i in range(0,len(List)):
    counter+=1
print(counter)

"""Write a Python program to change the position of every n-th value with the (n+1)th in a list.  
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]"""

"""
#swap x,y,z
z=x
x=y
y=z"""
List=[0,1,2,3,4,5]
expected_list=[]
temp=0
for i in range(0,len(List),2):
    temp=List[i]
    List[i]=List[i+1]
    List[i+1]=temp
    expected_list.append(List[i])
    expected_list.append(List[i+1])
print(expected_list)


"""Write a Python program to convert a list of multiple integers into a single integer. [11, 33, 50]
Expected Output: 113350"""

def convert_into_string(List):
    string=" "
    for i in List:
        string +=str(i)
    return string

print(convert_into_string([11,33,50]))


"""Write a Python program to compute the difference between two lists.  Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']"""


def differance_func(first_list,second_list):
    out_list1=[]
    out_list2=[]
    for i in first_list:
        if i not in second_list:
            out_list1.append(i)
    for j in second_list:
        if j not in first_list:
            out_list2.append(j)
    print(f"color1-color2: {out_list1}")
    print(f"color2-color1: {out_list2}")

differance_func(["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"])






    

