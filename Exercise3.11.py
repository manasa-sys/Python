#an algorithm that determines the greater value out of two numbers provided by the user
#program to calculate the greater number out of two numbers
num1=input('please enter first number: ')
num1=float(num1)
num2=input('please enter a second number')
num2=float(num2)
print('first number is :' + str(num1))
print('second number is '+ str(num2))
#condition to check greatest numbers
if(num1 > num2 ):
    print('the greatest number is : ' + str(num1))
else:
    print('the greatest number is : '+ str(num2))



