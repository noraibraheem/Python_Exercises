# for loop

numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(f"number is {number}")
else:
    print("all finishd")

print("*" * 10)

letters = "nora ibraheem"
for letter in letters:
    print(f"[{letter.upper().strip()}]")


# ranges
myrange = range(1, 11)
for rangee in myrange:
    print(rangee)

# loop on dictionary
myskills = {
    "html": "90%",
    "css": "80%",
    "js": "60%",
    "phb": "50%",
}
# print(myskills['js'])
# print(myskills.get("phb"))
for key in myskills:
    # print(key)  # print all key of dictionary
    # print keys and values
    print(
        f"my skills lang are { key .upper()} and thier progress are { myskills[key]} ")

# nested loop in dictionary
students = {
    "Ahmed":
    {"html": "90%",
     "css": "80%",
     "js": "60%",
     },
    "osama":
    {
        "html": "90%",
        "css": "80%",
        "js": "60%",
    },
    "ali":
    {
        "html": "90%",
        "css": "80%",
        "js": "60%",
    }
}
for name in students:
    print(f"student is {name} and has skills are:")
    for skill in students[name]:
        print(f"{skill} and its progress is {students[name][skill]}")
else:
    print("all is finished")

# another way to get elements from dictionary by nested loop
for main_key, main_value in students.items():
    print(f"{main_key} and its progress is: ")
    for child_key, child_value in main_value.items():
        print(f"-{child_key}-->{child_value}")
