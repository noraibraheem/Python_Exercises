#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between
first_name=input("")
last_name=input("")
print(first_name[::-1],last_name[::-1], sep=" ")

"""Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.  Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
string=input("")
print(list(string))
print(tuple(string))





"""Write a Python program to accept a filename from the user and print the extension of that. 
Sample filename : abc.java
Output : java"""
file_name=input(" ")
for i in range (len(file_name)):
    if file_name[i]==".":
        print(file_name[i+1:])




"""Write a Python program to display the first and last colors from the following list.  
color_list = ["Red","Green","White" ,"Black"]"""

color_list=["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[-1])


"""Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.  
Sample value of n is 5
Expected Result :155"""

num=int(input())
result=num+num*num+num*num*num
print(result)