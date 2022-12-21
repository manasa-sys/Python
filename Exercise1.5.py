#program that displays the volume of a rectangular prism after reading the dimensions of the prism
length=float(input('Enter the length: '))
while(True):
    if(length>0):
        break
    print("you entered a invalid length: please try again ")
    length=float(input('Enter another length: '))
width=float(input('Enter the width: '))

while(True):
    if(width>0):
        break
    print("You entered a invalid width: please try again ")
    width=float(input('Enter the width: '))

height = float(input('Enter the height: '))
while(True):
    if(height>0):
        break
    print("You entered a invalid height: please try again")
    height=float(input('Enter the height: '))

volume =float(length * width * height)
print('Volume of the rectangle is '+ str(volume))