
default_password = "nora@123"
input_password = input("enter your password: ")

tries = 3
while input_password != default_password:
    tries -= 1
    print(
        f"wrong password you have {'last' if tries==0 else tries } tries")
    input_password = input("enter your password: ")
    if tries == 0:
        print("all your tries are finished")
        break
        print("will not print")
else:
    print("correct password")
