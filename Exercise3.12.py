#program to calculate the tip for a server
#enter the total bill amount
amount=input('please enter the amount in the bill: ')
amount =float(amount)
TIP=0.15
while(True):
    if(amount>=1):
        Tip=(amount*TIP)
        print('Total tip to be paid is '+ str(Tip))
        Total_bill= amount +Tip
        print('total bill including tip to the server is '+ str(Total_bill))
        break
    print('please enter a valid amount to be paid(greater than 1$')

