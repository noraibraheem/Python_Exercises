#try--except--finally

try:
  number= int(input("enter your age: "))
except:
    print("enter integer value")
finally:
    print("your age is perfect")


try:
    #number=10/0
    #print(number)
    #print(x)
    y=5
    print(y)
except ZeroDivisionError:
    print("not allowed divided into zero")
except NameError:
    print("name error is found")
else:
    print("all values are true")
finally:
    print("you are chosen perfect value")