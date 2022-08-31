#iterable that contains date which can be iterated upon
#examples-->string,list,set,tuple,dictionary

mystring="Ahmed"
for i in  mystring:
    print(i,end=" ")
mylist=[1,2,3,4,5]
for i in mylist:
    print(i)

print("#"*20)
#iterator
#convert iterator into iterable by using iter () and loops it by using next()
mylist=[1,2,3,4]
myiterator=iter(mylist)
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))


#for i in "elzero" == for i in iter("elzero")