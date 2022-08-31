# bool

user = " "
print(user.isspace())

# true bool
print(bool("osama"))
print(bool("100"))
print(bool("100.95"))
print(bool([1, 2, 3, 4]))  # list

# false bool
print(bool(" "))
print(bool("0"))
print(bool("none"))
print(bool([]))
print(bool({}))
print(bool())


# boolean operators
age = 36
name = "ahmed"
print(age == 36 and name == "ahmed")
print(age == 36 or name == "ahmed")
print(age > 10)  # true
print(not age > 10)  # false
