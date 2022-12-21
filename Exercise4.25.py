#program to find the greatest number
num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
num3=int(input('enter the third number: '))
print('num1 is :'+ str(num1))
print('num2 is :' + str(num2))
print('num3 is : '+ str(num3))
if(num1>num2 and num1>num3):
    print('The greatest number is :'+ str(num1))
elif(num2>num1 and num2>num3):
    print('The greatest number is :'+ str(num2))
else:
    print('The greatest number is :'+ str(num3))
