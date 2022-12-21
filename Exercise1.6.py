#program for a salesperson.
commssion_pv=200.00
basesalary=400.00
#to find the number of vehicles sold
no_vehicle=int(input('Enter the number of vehicles sold: '))
print('number of vehicles is :'+ str(no_vehicle))
#to find total sale amount
amount=float(input('Enter the amount of total sales: '))
print('Amount of sales is : '+str(amount))
#To calculate the commission
commission= float(200*no_vehicle)
print('commission is '+'$'+str(commission))
#to calculate bonus
bonus=float(amount*0.05)
print('bonus is '+'$'+str(bonus))
# To calculate the total salary of the salesperson
Total_salary=float(basesalary+bonus+commission)
print('Total salary is '+ '$'+str(Total_salary))

