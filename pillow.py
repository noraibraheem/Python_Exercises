#pillow--->image mainipulation

from PIL import image
myimage=image.open("C:\Users\Administrator\Pictures\99127627_2471518773158252_7528474892702842880_n.jpg")
mybox=(300,300,800,800) #left,upper,right,lower
mynewimage=myimage.crop(mybox)
mynewimage.show()

'''myimage2=image.open("C:\Users\Administrator\Pictures\99127627_2471518773158252_7528474892702842880_n.jpg")
mybox=(200,200,500,500)
mynewimage2=myimage2.converted("L")  #converted from white to black
mynewimage2.show()'''