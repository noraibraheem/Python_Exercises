#built in function
#all() check if all elements of iteratible are true
x=[1,2,3,4]
if all(x):
    print("all values are true")
else:
    print("one element at least is false")



#any() check if one element at least is true
x=[1,2,3,[]]
if any(x):
    print("one elment at least is true")
else:
    print("all values are false")
#bin() returns binary value 
a=123
print(bin(a))
#id() returns an id of elemnt stored in memory
a=3
b=4
print(id(a))
print(id(b))
#sum(itratible,start) 
mylist=[1,2,4,6]
print(sum(mylist))
#range(start,end,step)

#abs
print(abs(-100))
print(abs(-4))
#min#max
mylist=[1,2,3,4,5,6,7]
print(min(mylist))
print(max(mylist))

#slice(start index,stop index,end)
mylist=[1,2,3,4,5,6,7]
print(mylist[:4])
print(mylist[slice(2,6)])  

#POW(base,exp,moduleus)
print(pow(2,5,10))

#enumerate function: make a counter on iteratable 

myskills=["html","css","c++","phb"]
myskillscounter=enumerate(myskills,1)
for counter, skill in  myskillscounter:
    print(f"{counter}{skill}")
    
 #reversed
myname="noraibraheem"
print(reversed(myname))
for letter in reversed(myname):
  print(letter)