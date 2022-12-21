#program to find whether one number is multiple of another
m=input('Please enter a number: ')
m=int(m)
print('m: '+str(m))
n=input('Please enter a number: ')
n=int(n)
print('n : ' + str(n))
remainder1=((m)%(n))
remainder1=float(remainder1)
print('The raminder is ' + str(remainder1) )
remainder2=float(n%m)
if(remainder1==0):
    print('m is multiple of n ')
elif(remainder2==0):
    print('n is  multiple of m ')
else:
    print('Neither m is multiple of n nor  n is multiple of m')

