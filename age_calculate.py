
# age calculate
age = input("your age is: ")
days = int(age) * 365
weeks = days / 7
hours = days * 24

unit = input("enter your age in days , weks , hours").strip().lower()
if unit == "weeks" or unit == "w":
    print(f"your age in weeks is {weeks}")

elif unit == "days" or unit == "d":
    print(f"your age in days is {days}")
elif unit == "hours" or unit == "h":
    print(f"your age in hours is {hours}")
else:
    print("you can't calcuLATE YOUR AGE".strip().lower())
