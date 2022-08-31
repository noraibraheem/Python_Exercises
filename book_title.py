file = open(r"C:\Users\Administrator\Desktop\ahmed.txt", "r")
for line in file:
      if line[-1] == "\n":
          print(line[0]+str(len(line)-1))
      else:
             print(line[0]+str(len(line)))

#your code goes here


file.close()