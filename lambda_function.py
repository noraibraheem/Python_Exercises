# lambda function
# it has no name
# you can call in inline without difining it
# you can use it in return data from another func
# lambda is one single expression not block of code
# lambda typ is function

def say_hello(name): return f"hello {name}"


print(say_hello("ahmed"))


def hello(name): return f"hello {name}"


# name_functon=lambda+parameter : statement
print(hello("abohashem"))
print(hello.__name__)
print(type(hello))
