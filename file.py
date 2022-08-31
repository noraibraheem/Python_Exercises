# read files
my_file = open("d:\python_projects\osama.txt", 'r')
# print(my_file.read())

# print(my_file.name) #print name of file
# print(my_file.encoding)
# print(my_file.mode) #read mode

# print(my_file.read(5))  # 5 is number of characters which will be read
# print(my_file.readline()) #read the first line only in file
# print(my_file.readlines())
# print(type(my_file.readlines()))

for line in my_file:
    print(line)
    if line.startswith(".5"):
        break

my_file.close()

# wrie files لو كتبت حاجه وبعدين مسحت الجمل دي وكتبت جديد فهوه تلفائي هيمسح القديم ده ويكتب الجديد ف الملف
myfile = open("d:\python_projects\write.txt", 'w')
myfile.write("welcome here sir\n")
myfile.write("i'm plessed to meet you sir")

mylist = ["ahmed \n", "nora \n", "mohammed \n", "ali \n"]
myfile.writelines(mylist)  # writelines recieve an list to write t in file

# append لو كتبت حاجه وبعدين مسحت السطور من هنا وعملت ابيند الجمل دي مش هتتمسح من الفايل وهيتم عمل ابيند للجمل بعديها

myfile = open("d:\python_projects\write.txt", 'a')
myfile.write("nora ibraheem")
myfile.write("abdelghany \n")
myfile.write("AI artificial intelligance\n")

