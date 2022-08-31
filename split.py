file_name=input(" ")
for i in range (len(file_name)):
    if file_name[i]==".":
        print(file_name[i+1:])

