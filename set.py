# set
# items are unique
# items aren't ordered and not have index
# slicing can't be done

myset = {1, 2, 3, 4, 1}
print(myset)

# set format
# clear()

a = {1, 2, 3, 4}
a.clear()
print(a)

# remove an element from set
a = {1, 2, 3, 4}
a.remove(4)
print(a)

# discard
a = {1, 2, 3}
a.discard(5)


# union--> union between two sets
a = {1, 2, 3}
b = {4, 5, 6}
print(a | b)
print(a.union(b))

# copy
x = {1, 2, 3}
y = x.copy()
print(y)

# add
d = {1, 2, 3, 4}
d.add(5)
print(d)

# pop
print(d.pop())

# differance (which fount in frist set and doesn't found in another)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6, 7}
c = a.difference(b)  # a-b
print(c)
# differance_update

a = {1, 2, 3, 4}
b = {3, 4, 5, 6, 7}
c = a.difference_update(b)
print(c)
print(a)


# intersection
a = {1, 2, 3, 4}
b = {4, 5, 6}
c = a.intersection(b)  # a&b
print(a)
print(c)

# intersection_update
a = {1, 2, 3, 4}
b = {4, 5, 6}
c = a.intersection_update(b)
print(a)
print(c)

# symmatric_differance(elements aren't common between two elements)

# issuperet
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {3, 4}
print(a.issuperset(b))  # false
print(a.issuperset(c))  # true

# issubset
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a.issubset(b))  # false(not all element of b are fund in set a)

# isdisjoint
a = {1, 2, 3}
b = {3, 4, 5, 6}
print(a.isdisjoint(b))  # false

a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))  # true
