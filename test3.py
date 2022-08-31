"""All_students=list(map(int,input().split()))
print(All_students)"""
dictionary={}
n=int(input("the number of elements"))
for i in range(n):
    keys=input()
    values=int(input())
    dictionary[keys]=values
    print(dictionary)
listelement=[]

for i in dictionary:
    print(i,dictionary[i])
    listelement.append(dictionary[i])
    final_list=sorted(set(list(listelement)))
    #final_list[-1]    #max value
    #final_list[-2]    #second_max_value
for j in dictionary:
    if final_list[-1]==dictionary[j]:
        print(j)
for k in dictionary:
    if final_list[-2]==dictionary[k]:
        print(k)




print(listelement)
print(final_list[-1])
print(final_list[-2])


