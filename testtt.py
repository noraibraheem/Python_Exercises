s="""w'o"w"""
print(repr(s)) #print the expression of string
print(str(s)) 
print(eval(s)) #evaluate a string and returns an object

b=frozenset('orange')
print(b)

name="nora"
age=34
print("my name is {} and my age is{}".format(name,age))
print("my name is{1}and my age is {0}".format(name,age))
print(f"my name is {name}and my age is{age}")

#boolean
#bool is a subclass of int but true or false is an instances of bool
print(issubclass(bool,int))
print(isinstance(True,bool))
