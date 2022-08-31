# function is a block of code to do a task
# function creats to prevent dry(don't repeat your self)
# func run when you call it
# func accepts parameters to deal with it
# func return data after job is finished
# there's built in functions and user defined functions


def func_def():
    print("hello world".strip().capitalize())


func_def()  # calling function


def fun_def():
    return "hello world ya shabab"


print(fun_def())

# add to numbers


def addition(num1, num2):
    if type(num1) != int or type(num2) != int:
        print("enter please integer numbers")
    else:
        print(num1+num2)


addition(5, "osama")

# print full name


def full_name(fname, mname, lname):
    print(
        f"your name is {fname.strip().capitalize()} {mname.capitalize().strip()} {lname.strip().capitalize()}")


full_name("nora", "ibraheem", "maged")

#packing and unpacking


def skills_func(*skills):
    for skill in skills:
        print(f"your skill is {skill}")


skills_func("html", "c++", "python", "css")


def food_menue(*foods):
    for meal in foods:
        print(f"your fav meal is {meal}")


food_menue("rice", "chicken", "fish")

# packing and unpacking for func arguments

skills = {
    "html": "80%",
    "css": "70%",
    "python": "90%"

}


def skills_func(**skills) ->dict: #type hinting
    for skill, value in skills.items():
        print(f"your skill is {skill}and your progress is {value}")


skills_func(**skills)

N=int(input())
A=set(map(int,input().split()))
n=int(input())

for i in range(0,n):
    cmd=input().split()
    if cmd[0]=="intersection_update":
        set_2=set(map(int,input().split()))
        if len(set_2)==cmd[1]:
            A.intersection_update(set_2)
    elif cmd[0]=="update":
        set_2=set(map(int,input().split()))
        if len(set_2)==cmd[1]:
            A.update(set_2)
        
    elif cmd[0]=="symmetric_difference_update":
        set_2=set(map(int,input().split()))
        if len(set_2)==cmd[1]:
            A.symmetric_difference_update(set_2)
        
    elif cmd[0]=="difference_update":
        set_2=set(map(int,input().split()))
        if len(set_2)==cmd[1]:
            A.difference_update(set_2)
print(sum(A))
"""16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66"""



