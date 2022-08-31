# MEMBERSHIP CONTROL ADD , DELETE , UPDATE names to admins list
admins = ["ahmed", "maged", "nora", "mohammed", "abohashem"]
name = input("enter your name please ?").strip()
if name in admins:
    print("you are an admin")
    option = input("you wanne update or delete ?!")
    print("option")
    if option == "update" or option == "u":

        newname = input("a new name please :")
        admins[admins.index(name)] = newname
        print(admins)
    elif option == "delete" or option == "d":

        admins.remove(name)
        print(admins)
else:
    print("you aren't admin")
    choice = input("ARE you want to be admin Y /N ?").strip().capitalize()
    if choice == 'y' or choice == 'Y':
        admins.append(name)
        print(admins)
    elif choice == 'n' or choice == 'N':
        print("you aren't added")
