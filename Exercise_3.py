#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment_1 
Exercise_3

Created on Mon Sep  5 00:14:30 2022

@author: 
    Manasa Manohara Shetty
    Manisha Bhardwaj
    Darlene Tverdohleb
    Chen Zhang
"""

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(x)
        return True
    except (TypeError, ValueError):
        pass
    return False

# 11 –	Develop an algorithm that determines the greater value 
#       out of two numbers provided by the user. Display this value. 

n1 = input("Please enter your first number: \n")
while True:
    if is_number(n1) == True:
        n1 = float(n1); 
        if n1 >= 0:
            break
    n1 = input("You entered a wrong number, please re-enter your first number: \n")

n2 = input("Please enter your second number: \n")
while True:
    if is_number(n2) == True:
        n2 = float(n2); 
        if n2 >= 0:
            break
    n2 = input("You entered a wrong number, please re-enter your second number: \n")
    
if n1 == n2:
    print("Two numbers are same", n1, n2);
elif n1 < n2:
    print(n2, "is greater");
else:
    print(n1, "is greater");
    
print("\n===========================\n")
    
    
# 12 –	Write an algorithm that determines the amount to pay as a tip to a server in a restaurant. 
#       The tip should be 15% when the bill is at least $1.    

amount = input("Please enter the amount: \n")
while True:
    if is_number(amount) == True:
        amount = float(amount); 
        if amount >= 0:
            break
    amount = input("You entered a wrong number, please re-enter the amount: \n")

if amount > 1:
    total = amount + amount * 0.15
else:
    total = amount
    
print("Total amount: $", "%.2f" %total);

print("\n===========================\n")

# 13 –	A computer store sells diskettes at a price of $1 each for small orders. 
#       The store sells them at a price of 70 cents each for orders of 25+ units. 
#       Furthermore, if you are a member of Club Z, the store will give you an extra discount of 2%.
#       Write an algorithm that determines the total price for a purchase. 


diskettes = input("How many diskettes do you want? \n")
while True:
    if diskettes.isdigit() == True :
        diskettes = int(diskettes);
        if diskettes >= 0:
            break
    diskettes = input("You entered a wrong number, How many diskettes do you want?: \n")

member = input("Are you a member of Club Z? (Y/N) \n")
if member == "Y" or member == "y":      
    if diskettes >= 25:
        total_price = (0.7 * diskettes) * 0.98
    else:
        total_price = diskettes * 0.98
else:
    if diskettes >= 25:
        total_price = 0.7 * diskettes
    else:
        total_price = diskettes
    
print("total price:" ,"%.2f" %total_price);

print("\n===========================\n")


# 14 –	A print shop charges 5 cents per copy for the first 100 copies. 
#       For any subsequent copies, they charge 3 cents each. 
#       Write an algorithm that determines the price associated with a given number of copies. 


pages = input("Please enter the number of pages: \n")    
while True:
    if pages.isdigit() == True :
        pages = int(pages);
        if pages > 0:
            break
    pages = input("You entered a wrong number, please re-enter the number of pages: \n")

if pages <= 100:
    total_price = pages * 0.05
else:
    total_price = 5 + (pages - 100) * 0.03
    
print("total_price: $","%.2f" %total_price)

print("\n===========================\n")


# 15 –	Write an algorithm that simulates the withdrawal of an amount of money from an ATM. 
#       The algorithm should ask for the amount of the current balance 
#       and the amount of the withdrawal. 
#       If the amount of the withdrawal is greater than the balance, 
#       display an error message; otherwise, display the new balance. 

balance = 2000;

withdraw = input("Your balance is ${}, How much do you want to withdraw?\n".format(balance))
while True:
    if withdraw.isdigit() == True:
        withdraw = int(withdraw);
        if balance > withdraw > 0:
            break
    withdraw = input("You have insufficient balance, please re-enter the amount: \n")

new_balance = balance - withdraw;
print("Withdraw: $", withdraw);
print("Your new balance: $", new_balance);

print("\n===========================\n")


# 16 –	An electricity bill is calculated by obtaining the number of days for 
#       which electricity is supplied and the number of kilowatt hours (kWh) consumed. 
#       The client is billed at a rate of $0.50 per day and $0.30 per kWh. 
#       For a client that has consumed more than 200 kWh, 
#       their rate is reduced from $0.30 to $0.20 for additional kWh. 
#       We want to obtain the total amount for the bill.

days = input("Please enter the number of days: \n")    
while True:
    if days.isdigit() == True :
        days = int(days);
        if days >= 0:
            break
    days = input("You entered a wrong number, please re-enter the number of days: \n")
    
kWh = input("Please enter the number of kWh: \n")    
while True:
    if kWh.isdigit() == True :
        kWh = int(kWh);
        if kWh >= 0:
            break
    kWh = input("You entered a wrong number, please re-enter the number of kWh: \n")
    
if kWh <= 200:
    bill = days * 0.5 + kWh *0.3 
else:
    bill = days * 0.5 + 60 + (kWh -200) * 0.2
   
print("Your bill: $", bill)   

print("\n===========================\n")

# 17 –	Write an algorithm that reads an integer and determines whether it is even or odd.
 
integer = input("Please enter an integer: \n")    
while True:
    if integer.isdigit() == True :
        integer = int(integer);
        if integer >= 0:
            break
    integer = input("You entered a wrong number, please re-enter an integer: \n")
    
if integer % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")

print("\n===========================\n")


# 18 –	Write an algorithm that reads two integers m and n and determines whether m is a multiple of n.

m = input("Please enter the first integer: \n")    
while True:
    if m.isdigit() == True :
        m = int(m);
        if m >= 0:
            break
    m = input("You entered a wrong number, please re-enter an integer: \n")

n = input("Please enter the second integer: \n")    
while True:
    if n.isdigit() == True :
        n = int(n);
        if n >= 0:
            break
    n = input("You entered a wrong number, please re-enter the other integer: \n")
    
if m % n == 0:
    print("{} is a multiple of {}" .format(m,n))
else:
    print("{} is not a multiple of {} ".format(m,n))
    
print("\n===========================\n")


# 19 –	Give an algorithm that reads three numbers (a, b, c) 
#       and determines whether any one of the numbers is equal to the sum of the other two. 
#       If such a number exists, display it; otherwise, display the message “No solution”.

a = input("Please enter the first number: \n")
while True:
    if is_number(a) == True:
        a = float(a); 
        if a > 0:
            break
    a = input("You entered a wrong number, please re-enter the first number: \n")

b = input("Please enter the second number: \n")
while True:
    if is_number(b) == True:
        b = float(b); 
        if b > 0:
            break
    b = input("You entered a wrong number, please re-enter the second number: \n")
    
c = input("Please enter the third number: \n")
while True:
    if is_number(c) == True:
        c = float(c); 
        if c > 0:
            break
    c = input("You entered a wrong number, please re-enter the third number: \n")

if (a == b + c): 
    print("{}={}+{}".format(a,b,c))
elif (b == a + c):
    print("{}={}+{}".format(b,a,c))
elif (c == a + b):
    print("{}={}+{}".format(c,a,b))
else:
    print("No solution")  



    