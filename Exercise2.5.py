#Expenses of Monique
#weekly food expenses of Monique
food_expense =(input('Please enter the food expenses for a week: '))
food_expense = float(food_expense)
print('Food expenses for a week is '+ '$'+str(food_expense))

#weekly common expenses of Monique
comm_expenses = input('Please enter the common expenses for a week: ')
comm_expenses = float(comm_expenses)
print('Common expenses for a week is '+'$'+ str(comm_expenses))
#food expenses for a month
foodexpense_month=float(food_expense *4)
#common expenses for a month
commexpenses_month=float(comm_expenses *4)

print('Food expenses for a month are :' +'$'+str(foodexpense_month))
print('Common expenses for a month are :' +'$'+ str(commexpenses_month))
#monthly transit expenses
transit_expenses= input('Please enter the transit expenses for a month: ')
transit_expenses = float(transit_expenses)
print(' Monthly transit expenses is: '+'$'+ str(transit_expenses))
#monthly rent expenses
rent_expenses= input ('Please enter the amount of rent for a month: ')
rent_expenses =float(rent_expenses)
print('Monthly rent to be paid is: '+'$'+ str(rent_expenses))
#monthly bills
monthly_bills =input('please enter the monthly bills:  ')
monthly_bills = float(monthly_bills)
print('Total monthly bill amount is:' + '$'+str(monthly_bills))
#paycheque amount
paycheque_amount=input('Please enter the amount of one paycheque: ')
paycheque_amount = float(paycheque_amount)
print('Amount of one paycheque is '+ '$'+str(paycheque_amount))
#total monthly income
Total_income=float(paycheque_amount*2)
print('Total monthly income is :'+'$'+ str(Total_income))
#to calculate the total expenses
Total_expenses= float(foodexpense_month +commexpenses_month +transit_expenses +rent_expenses+
                      monthly_bills)
print('Total monthly expeses is :' +'$'+ str(Total_expenses))
#to calculate the total savings
saving_month=float(Total_income-Total_expenses)
print('Total saving per month is :' +'$'+ str(saving_month))
