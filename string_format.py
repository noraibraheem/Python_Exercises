# string_formatting

print("my name is %s and my age is %d " % ("nora", 21))
name = "nora"
age = 21
print("my name is %s anmd my age is %d " % (name, age))

astring = "hello everyone , i'm pleased to meet you all"
print("%s" % astring)
print("%.5s" % astring)


# new formatting
name = "nora"
age = "21"
print("my name is {} and my age is {}".format(name, age))

x = 123456743
print("my money in bank is {:d}".format(x))

a = 11
b = 12
c = 13
print("numbers are:\n{0}\n{2}\n{1}".format(a, b, c))
print("numbers are:\n{1}\n{2}\n{0}".format(a, b, c))
print("numbers are:\n{}\n{}\n{}".format(c, b, a))

# version 3.6 up
name = "nora"
age = 21
print(f"my name is {name} and my age is {ager}")
