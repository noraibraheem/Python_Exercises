#filter out all elements for which the function returns true

def check_numbers(number):
    return number>10
mylist=[1,2,3,10,23,44,55]
for num in filter(check_numbers,mylist):
    print(num)

#filter with list of names
def check_names(name):
    return name.startswith("o")
mylist=["omar","osama","oka","ahmed"]
for name in filter(check_names,mylist):
    print(name)
print("*"*50)
#filter with lambda function
mylist=["omar","osama","oka","ahmed"]
for name in filter((lambda name:name.startswith("o")),mylist):
    print(name)


#reduce take a function and iterable as filter and map
from functools import reduce
def sum_num(x,y):
    return x+y
mylist=[1,1,2,4,5] #sum=13
result= reduce(sum_num,mylist)
print(result)
print("#"*50)
#reduce with lambda function
from functools import reduce
mylist=[1,1,2,4,5] #sum=13
result=reduce((lambda x,y:x+y),mylist)
print(result)