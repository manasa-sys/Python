#program for withdrawal aof amount in ATM
#to find the initial balance before withdawal
current_balance= input('please enter the current balance: ')
current_balance = float(current_balance)
print('current balance in the account is :' + str(current_balance))
#To find the withdawal amount
withdrawal_amount=input('please enter the amount to be withdrawn: ')
withdrawal_amount = float(withdrawal_amount)
print('current withdrawal amount is '+ str(withdrawal_amount))

if(withdrawal_amount > current_balance):
    print('Insufficient balance..Please enter another amount')

elif(current_balance>withdrawal_amount):
    remaining_balance= current_balance - withdrawal_amount
    print('The new balance in your account is '+ str(remaining_balance))
    print('Thank you for using our ATM service')
