"""we have two lists, we want to make them a list making pairs with"""
a=[1,2,3]
b=[4,5,6]
print(list(zip(a,b)))


"""Iterables with Different Length"""
x = [1, 2, 3, 4]
y = ['one', 'two']
z = ['I', 'II', 'III']
result = zip(x, y, z)
print(list(result))


"""unzip / unpack items"""
x = [1, 2, 3]
y = ['one', 'two', 'three']
result = zip(x, y)

# unzip
a, b = zip(*result)
print(a)
print(b)


"""You can create a dictionary with list of zipped keys and values"""
keys=['name','age']
values=['nora','21']
print(dict(zip(keys,values)))

"""Using zip() function you can loop through multiple lists at once"""
x = [1, 2, 3]
y = ['one', 'two', 'three']
for a,b in zip(x,y):
    print(a,b)

my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)


my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)







my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for key, value in sorted(my_dict.items()):
    print(key,value)


my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for key, value in sorted(my_dict.items()):
    print(key,end=" ")
print(end='\n')
for i in my_dict:
    for j in my_dict[i]:
        print(j,end=" ")
        if(j==3 or j==7):
            print(end="\n")

