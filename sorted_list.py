


List=[]
while True:
    try:
        num=input("enter plz number")
        if num=="done":
            break
        number=int(num)
        List.append(number)
        y=sorted(set(list(List)))
          
    except ValueError:
        print("invalid number")

print(y)
print(y[0])
print(y[-1])






