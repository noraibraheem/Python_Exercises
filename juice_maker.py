class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')
    def __add__(self,newjuice):
        self.name+='&'+str(newjuice.name)
        self.capacity+=newjuice.capacity
        return self.__str__





a = Juice('Orange', 1.5)  #orange(1.5L)
b = Juice('Apple', 2.0)   #Apple(2.0L)
#.split()-->split int sub strings
# .strip()-->removes all white spaces

print(a.__add__(b)())



List=[1,-2,3,-3]
no_negatives=0
for i in List:
    if i<0:
        no_negatives+=1
print(no_negatives)

#list comprehensive
print(len([num for num in List if num<0]))



"""Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
def elementwise_greater_than(L, thresh):
    Listt=[]
    for i in range(0,len(L)) :
        if L[i]>thresh:
           Listt.append(True)
        else:
            Listt.append(False)
    print(Listt)

elementwise_greater_than([1, 2, 3, 4], 2)


"""
Takes a list of documents (each document is a string) and a keyword. 
Returns list of the index values into the original list for all documents 
containing the keyword.
Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]"""


#solution
def word_search(doc_list, keyword):
    doc_list=[]
    for i in range(0,len(doc_list)):
        for j in doc_list[i]:
            if doc_list[i][j]==keyword:
                break
        print(doc_list[i])
doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
word_search(doc_list, 'casino')