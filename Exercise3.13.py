#Enter the number of diskettes
no_of_disk= int(input('please enter the number of diskettes: '))
if(no_of_disk<0):
    print('please enter a valid number: ')
#when number of disquettes is less than 25,price per disquette is 1$
elif(no_of_disk<=25):
    total_price=1*no_of_disk
    print('total price to be paid is:' + str(total_price))
#when the number of disquettes is greater than 25 price per disquette is 0.7cents
elif(no_of_disk>25):
    total_price=0.7*no_of_disk
    print('total price to be paid is : '+ str(total_price))
member=input('Are you a member of Club Z(Y/N): ')
if(member=='y' or member=='Y'):
    total_price=total_price-(0.02*total_price)
    print('total amount to be paid for the members of the club Z are :'+str(total_price))








