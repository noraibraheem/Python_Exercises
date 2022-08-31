import collections
from typing import NamedTuple, OrderedDict


"""collections>>Counter,NamedTuple,OrderedDict,defaultdict,deque"""

"""1)Counter: is a countainer that stores elements as dictionary keys in thier counts as dictionary values"""
from collections import Counter, defaultdict, namedtuple
string="aaaaaabbbbbcccccc"
my_counter=Counter(string)
print(my_counter)
#if we wanne to calculate the most common value of string
print(my_counter.most_common(1))
print(my_counter.most_common(2))

"""2)namedtuple has two argument one of them is a class and another which gave it values"""
from collections import namedtuple
part=namedtuple('part','x,y')
pt=part(5,4)
print(pt)
print(pt.x,pt.y)

"""3)ordered dict ids just like a regular dictionary but they remember the order that the items were inserted
Print each key and value as tuple in long list"""
from collections import OrderedDict
ordered_dic=OrderedDict()
ordered_dic['a']=1
ordered_dic['b']=2
ordered_dic['c']=3
ordered_dic['d']=4
print(ordered_dic)


"""4)deque >>list"""
from collections import deque
d=deque()
d.append(1)
d.append(2)
d.append(3)
print(d)

"""5)defaultdict :when an iteratable is passed as default argument ,A defaultdict then created with values that are list """
from collections import defaultdict
#Defining a dict
d = defaultdict(list)
  
for i in range(5):
    d[i].append(i)
      
print("Dictionary with values as list:")
print(d)
