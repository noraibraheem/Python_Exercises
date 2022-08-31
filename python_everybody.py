import random
value=random.randint(2,6)
print(value)  #giving an integer random value is fallen between 2 and 6
value=random.random()
print(value)  
names=['ahmed','ali','mohammed','hend']
value=random.choice(names)
print(value) #choice a random name between a group of names
color=['red','yellow','black','blue']
value=random.choices(color,k=4)  #choice a random values of colors between a group of colors
print(value)



for i in [2,1,5]:
    print(i)



fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])