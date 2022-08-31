
################imojii converter code ####################
def imojii_converter(message):
    words=message.split(" ")
    imojii={
        '!' : ':)',
        '#' : ':('

    }
    output=" "
    for word in words:
        output+=imojii.get(word,word)+" "
    return output


message=input("<")
print(imojii_converter(message))
    
