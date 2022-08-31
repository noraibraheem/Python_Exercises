def skills_func(*skills):  
    for skill in skills:
        print(f"your skill is {skill}")


skills_func("html", "c++", "python", "css")

skills = {
    "html": "80%",
    "css": "70%",
    "python": "90%"

}


def skills_func(**skills):
    for skill, value in skills.items():
        print(f"your skill is {skill}and your progress is {value}")


skills_func(**skills)


