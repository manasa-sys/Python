#program to calculate the taxes
salary=(input('Please enter a salary:'))
salary=float(salary)
if(0.00<=salary<=18,000.00):
    taxRate=0.1
elif(18,000.01 <= salary <=32,000.00):
    taxRate=0.2
elif(32,000.01 <=salary <=60,000):
    taxRate=0.3
elif(salary>60000.00):
    taxRate=0.4
married=input('Are you married(y/n)')
if(married=='Y' or married=='y'):
    taxRate=taxRate-0.02

child_no=input('how many children do you have')
child_no=int(child_no)
if(child_no>0):
    taxRate=taxRate-(child_no*0.005)

newlyarrival=input('Are you new arrival(y/n)')
if(newlyarrival=='Y' or newlyarrival=='y'):
    taxRate=taxRate-0.08

if taxRate<0:
    taxRate=0

Total_tax=salary*taxRate
print('Total tax is: '+str(Total_tax))
Total_saving=salary-Total_tax
print('total saving is: '+str(Total_saving))