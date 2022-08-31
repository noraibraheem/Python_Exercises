from sys import implementation


smallest=None
print("before")
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest=value
    elif smallest>value:
        smallest=value
    print(smallest,value)
print("after",smallest)



"""x=int(input())
y=int(input())
z=int(input())
n=int(input())
List=[]
for a in range(0,x+1):
    for b in range(0,y+1):
        for c in range(0,z+1):
            List.append([a,b,c])
print(List)"""
List=[1,2,3,4,4,5,6]
x=sorted(set(list(List)))
print(x)


#nested list
"""N_stu=int(input())
d={}
scores=[]
for i in range(0,N_stu):
    name=input()
    score=float(input())
    d[name]=score
    scores.append(score)
new_scores=sorted((list(scores)))
value=new_scores[1]
for i in d:
    if d[i]==value:
        print(i)"""

"""
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
query_scores = student_marks[query_name]
print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))"""


def print_full_name(first, last):
    print(f"Hello {first} {last}! You just deloved into python")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)