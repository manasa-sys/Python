#program that calculates an employee’s gross salary for a week,
# given their hourly rate and the number of hours worked.
#gross salary for a week
no_hours=float(input('Enter the number of hours: '))

while(True):
    if(no_hours>0):
        break
    print('wrong value.please enter valid number of hours')
    no_hours=float(input('Enter the number of hours: '))

#enter the hourly rate
hour_rate=float(input('Enter the hourly rate: '))
while(True):
    if(hour_rate>0):
        break
    print('wrong value.please enter another value')
    hour_rate=float(input('Enter the hourly rate: '))
#To calculate gross salary
gross_salary= float(no_hours *hour_rate)
print('gross salary is : '+ str(gross_salary)+'$')
