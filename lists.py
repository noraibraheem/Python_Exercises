# LIST
# can ba modified(append,insert,remove , clear)
# hasn't unque elements
# list are ordered each element has an index
# lists have different types

mylist = ["one", 2, "two", "three", "four", 5]
print(mylist)
print(mylist[1])
print(mylist[4])

mylist[2] = "two"

print(mylist[::2])
print(mylist[0:4])
print(mylist[::1])

mylist[0:3] = ["a", "b", "c"]
print(mylist)

# methods of list
# append-->add item to the list from end
mylist = ['one', 'two', 'three', 'four']
print(mylist.append('five'))

mylist2 = ["one", 2, "two", "three", "four", 5]
mylist.append(mylist2)
print(mylist)
print(mylist[4])
print(mylist[5])
print(mylist[5][1])

# extend
a = [1, 2, 3]
b = ['one', 'two', 'three']
a.extend(b)
print(a)

# sort --> integers values only
a = [1, -3, 10, 0, -15]
a.sort(reverse=True)
print(a)
a.sort(reverse=False)
print(a)

# remove
a = [1, 2, 3, 4, 5, 6]
a.remove(5)
print(a)

# reverse --> integers and strings
b = ['one', 'two', 'three', 1, 3, 4]
b.reverse()
print(b)

# clear --> clear all elements in list
a = [1, 2, 4, 5, 6]
a.clear()
print(a)

# copy
a = [1, 3, 4, 5]
b = a.copy()
print(a)
print(b)

# index
a = [1, 2, 3, 4, 5, 6, 7]
print(a.index(5))

# insert --> insert element at particular index
a = [1, 2, 3, 4, 5, 6]
a.insert(3, 5)
print(a)

# pop(index)
a = [1, 2, 3, 4, 5]
print(a.pop(3))
