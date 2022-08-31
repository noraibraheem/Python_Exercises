x=y=[1,2,3]
x=[3,4,5]
print(y)

x=y=[1,2,3]
x[0]=5
print(y)

List=[1,'ali',3.4]
print(List[1])
#list is an ordered collection with unique values
#SET is an unordered collection with unique values
a={1,2,'ali'}
#dict is an unordered collection of unique pairs of keys and values
normal='foo\nbar'
print(normal)
escaped='foo\\bar'
print(escaped)
raw=r'foo\nbar'
print(raw)

"""def wrap(string, max_width):
        
        
                
    return "\n".join([string[i :i+max_width]for i in range(0,len(string))])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
"""

x="ali ahmed"
for i in range(0,len(x)):
    if x[i]==" ":
        print(x[0:i].capitalize()+" "+x[i+1:].capitalize())
        

    
def solve(s):
    if 0<len(s)<1000:
        for i in range(0,len(s)):
            if s[i]==" ":
                print(s[0:i].capitalize()+" "+s[i+1:].capitalize())

s=input()
solve(s)


my_list=[1,2,3]
my_set=set(my_list)
print(my_set)
        

my_dict={
    'ali':'23',
    'ahmed':'22',
    'nora':'20'
}
from collections import defaultdict
my_dict=defaultdict(lambda:"15")
print(my_dict["nor"])





        
    



