try:
    
    var = input('Enter input: ')  
    key, value = var.split()
    d = {key: int(value)}         
    print(d)
    
except ValueError:
    print('Incorrect format supplied, type "id 1230" expected. Please try again.')


"""dictionary=dict()
data=input("enter name and score :")
temp=data.split(':')
dictionary[temp[0]]=int(temp[1])

for key,value in dictionary.items():
    print('name:{},score:{}'.format(key,value))"""



#enter elements into dictionary by using map
d={}
n=int(input("the number of elements"))
for i in range(n):
    keys=input()
    values=int(input())
    d[keys]=values
    print(d)