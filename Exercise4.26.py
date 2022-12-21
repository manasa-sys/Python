#program to display the numbers in ascending order
num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
num3=int(input('enter the third number: '))
print('num1 is :'+ str(num1))
print('num2 is :' + str(num2))
print('num3 is : '+ str(num3))

if(num1<=num2<=num3):
    print(num1,num2,num3)
elif(num1<=num3 <=num2):
    print(num1,num3,num2)
elif(num2<=num1<=num3):
    print(num2,num1,num3)
elif(num2<=num3 <=num1):
    print(num2,num3,num1)
elif(num3<=num1<=num2 ):
    print(num3,num1,num2)
elif(num3<=num2<=num1):
    print(num3,num2,num1)
