#program to calculate the electricity bill

no_days=float(input('Please enter the number of days the electricity is used: '))
print('Number of days the electricity used is :'+str(no_days))
no_kWh=float(input('Please enter the number of units of power consumed in kWh: '))
print('Amount of power consumed in kWh is: '+str(no_kWh))
#
if(no_kWh<=200):
    Total_bill= float((0.50*no_days) +(0.30*no_kWh))
    print('Total bill is : '+str(Total_bill))
elif(no_kWh>200):
    Total_bill = float((0.50*no_days) +(0.20*no_kWh))
    print('Total bill is : ' + str(Total_bill))
