# email

name = "Nora"
email = "noramaged@elzero_org"
username = email[0:email.index("@")].strip().capitalize()
print(f"user name is: {username}")
website = email[email.index('@')+1:].strip().capitalize()
print(f"web site is: {website}")
