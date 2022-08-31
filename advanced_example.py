
my_file=None
tries=5
while tries>0:
    try:
        print("enter the ile name with absolute value to open")
        print(f"you have {tries}are left")
        file_name_path=input("file_name=>").strip()
        the_file=open(file_name_path,'r')
        print(the_file.read())
    except FileNotFoundError:
        print("your file name is not valid please enter valid name")
        tries-=1
    finally:
        if my_file is not None:
            file.close()
            print("closed file")



else:
    print("all tries are done")