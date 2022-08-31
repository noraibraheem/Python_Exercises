#zip returns a zip object which contains all objects
#zip()length is the length of lowest objects



list1=[1,2,3,4,5]
list2=[1,2,3,4]
tuple1=("ali","ahmed","mohamed","nora")
dictionary={"name":"ahmed","age":23,"level":"graduated"}

for item1,item2,item3,item4 in zip(list1,list2,tuple1,dictionary):
    print("item of list1 is ->",item1)
    print("item of list2 is ->",item2)
    print("item of tuple is ->",item3)
    print("key of dictionary is ->",item4)
    print("value of dictionary is ->",dictionary[item4])