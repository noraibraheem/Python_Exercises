import datetime
#print current date and time
print(dir(datetime))
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)

#print special day
print(datetime.datetime(2021,7,16))

#print minutes of time
print(datetime.datetime.now().minute)

#print seconds of time
print(datetime.datetime.now().second)

#print rhe start and the end of date
print(datetime.datetime.min)
print(datetime.datetime.max)

#calculate number of days which lived
birthday_date=datetime.datetime(2000,8,28)
current_date=datetime.datetime.now()

print(f"you lived {(current_date-birthday_date).days} days.")

#strftime 
import datetime
mybirthday_date=datetime.datetime(2000,8,28)
print(mybirthday_date.strftime("%b"))  #concise month
print(mybirthday_date.strftime("%B"))  #full month
print(mybirthday_date.strftime("%A"))  #full day
print(mybirthday_date.strftime("%a"))  #concise day
print(mybirthday_date.strftime("%d %B %Y"))
