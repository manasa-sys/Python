#program to check whether any one of the number is equal to sum of the other two
a=int(input('enter a number a :'))
b=int(input('enter a number b :'))
c=int(input('enter a number c :'))
print('first number is :' + str(a))
print('second number is :' + str(b))
print('third number is :' + str(c))
num1=a+b;
num2=b+c;
num3=c+a;
if(num1==c):
    print('sum of a+b is: '+str(num1))
elif(num2==a):
    print('sum of b+c is: '+ str(num2))
elif(num3==b):
    print('sum of c+a is:'+ str(num3))
else:
    print('No solution')

