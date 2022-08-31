secret_num=16
guess_count=0
while guess_count<3:
    user_guess=int(input("your guess is : "))
    guess_count+=1
    if user_guess==secret_num:
        print("you are winner!")
        break
else:
    print("Sorry,you are failed")
    
