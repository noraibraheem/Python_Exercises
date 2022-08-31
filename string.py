mystring = "I Love Python"
print(mystring[0])
print(mystring[-1])
print(mystring[3])
print(mystring[1:4])
print(mystring[1:])
print(mystring[:5])
print(mystring[::2])
print(mystring[:: 3])

print(len(mystring))  # length of string


mystring = "### i love python #####"  # stripping string
print(mystring.strip("#"))
print(mystring.rstrip("##"))
print(mystring.lstrip("##"))


mystring = "Osama mOhammed Elzeroo"
print(mystring.upper())
print(mystring.lower())
print(mystring.title())

a, b, c = "1", "11", "111"  # zfill
print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))

# split
astring = "i love python and c++"
print(astring.split())

astring = "i-love-python-and-phb"

print(astring.split("-"))
print(astring.split("-", 2))
print(astring.rsplit("-", 2))


# center
astring = "osama"
print(astring.center(9, "%"))
print(astring.center(12, "#"))

# rjust
astring = "osama"
print(astring.rjust(9, "%"))
print(astring.ljust(12, "#"))

# count
a = "i love python , c++, css html and css"
print(a.count("css"))

# swapcase start switch endswitch
astring = "I l_ove AHmed"
print(astring.swapcase())
print(astring.startswith("A"))
print(astring.endswith("d"))

# index

astring = "i love python"
print(astring.index("p"))
print(astring.index("p", 0, 10))  # index(char,start,end)

# find

print(astring.find("p", 1, 5))


# title #istitle
astring = "nora ibraheem 32g"
print(astring.title())
print(astring.istitle())

# isidentifier
astring = "nora_ibraheem"
print(astring.isidentifier())


# split lines
astring = """ first 
second
 three """
print(astring.splitlines())

# expand tabs
astring = "nora\ibraheem\abdelghany"
print(astring.expandtabs(3))
x = "aaaaaaaaaAAAAAAAAPPP"
print(x.isalpha())
y = "owwwe333"
print(y.isalpha())

#replace (oldvalue, newvalue, count)
astring = "one second three one one"
print(astring.replace("one", "1"))
print(astring.replace("one", "1", 2))
print(astring.replace("one", "1", 3))

# join --> convert list into string
list = ["one", "two", "three", "four"]
print(type("-".join(list)))




########################################## HOW TO REMOVE A DUPLICATED ITEMS FROM string#######################33
def remove_duplicated_items(string):
    List=string.split(" ")
    result=[]
    for word in List:
        if word not in result:
            result.append(word)
    return " ".join(result)   #to convert thus list into string again

print(remove_duplicated_items("hello hello sir sir in our country"))


def remove_duplicate_items(sentance):
    return " ".join(list(dict.fromkeys(sentance.split(" "))))

print(remove_duplicate_items("my name is nora nora ibraheem ibraheem"))