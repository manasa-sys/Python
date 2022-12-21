#program to check whether the number is even or odd
num1=int(input('Please enter a inetger: '))
print('num1 is:'+str(num1))
while(True):
    if(num1>0):
        break
    print('Please enter a number greater than zero ')
    num1=int(input('Please enter another inetger: '))
if(num1%2== 0):
        print('The entered number is even ')
else:
        print('The enetered number is odd')



