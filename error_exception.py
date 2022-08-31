#لو الشرط متحققش ده معناه ان ف غلط ف الحته دي فمينفعش يكمل الكود عادي كده
#x="ahmed"
#if type(x)!=int:
    #raise ValueError("only integer values are allowed")

y=-10
if y<0:
    raise Exception("only values greater than 0 are allowed")
else:
    print("alright")