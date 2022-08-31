#map
#[1] map take a function and iterator
#[2] map called map because it map the function on every element
#[3]the function can be pre-defined function or lambda function

#PREDEFINED FUNCTION #map(function,list)
def format_text(text):
    return f"-{text .strip().capitalize()}-"
mylist=["ahmed","nora","ali"]
for name in map(format_text,mylist):

    print(name)
print("#"*50)
#lambda function
mylist=["ahmed","nora","ali"]
for name in map(lambda text: f"-{text}-",mylist):
    print(name)
