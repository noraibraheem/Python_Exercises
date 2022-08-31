# dictionary
# dict items are arounded by brackets
# dict items aren't ordered , are unique
# dict values can be any type of data types
# dict consist of key:value

user = {"name": "nora", "age": "21", "countrey": "sadat city"}
print(user)
print(user['countrey'])
print(user["age"])

# 2 D dictionary
languages = {'one': {'name': 'html', 'progress': '90%'}, 'two': {'name': 'css', 'progress': '80%'}
             }
print(languages)
print(languages['one'])
print(languages['one']['name'])

# dictionary methods
# copy
member = {"name": "nora", "age": "21"}
two = member.copy()
print(two)

# clear
member = {"name": "nora", "age": "21"}
print(member.clear())

# keys+values
user = {"name": "nora", "age": "21", "countrey": "sadat city"}
print(user.keys())
print(user.values())

# update
user = {"name": "nora", "age": "21", "countrey": "sadat city"}
user.update({"level": "three"})
print(user)

# fromkeys
a = ('mykeyone', 'mykeytwo', 'mykeythree')
b = 'x'
print(dict.fromkeys(a, b))

# popitem
user = {"name": "nora", "age": "21", "countrey": "sadat city"}
print(user.popitem())
user.update({'level': 'three'})
print(user.popitem())

# setdefault
user = {"name": "nora", "age": "21", "countrey": "sadat city"}
print(user.setdefault("name", "osama"))
