#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment_1 
Exercise_1

Created on Sun Sep  4 23:48:44 2022

@author: 
    Manasa Manohara Shetty
    Manisha Bhardwaj
    Darlene Tverdohleb
    Chen Zhang
"""

#import constant

# print(constant.GST_rate);
# print(constant.QST_rate);

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


# 2 – In the old system of calculating sales tax in Québec, 
#     the taxes on a product were 7% for the GST, and 7.5% for the QST 
#     (applied after calculating the GST). 
#     Make a program that reads the unit price of a product and the quantity purchased,
#     and that displays the amounts for the GST, the QST, and the total price after taxes. 
    
GST_rate = 0.07;
QST_rate = 0.075;

price = input("Please enter the single item price: \n")

while True:
    if is_number(price) == True:
        price = float(price); 
        if price > 0:
            break
    price = input("You entered a wrong number, please re-enter the single item price: \n")
      
quantity = input("Please enter the quantity: \n")
    
while True:
    if quantity.isdigit() == True :
        quantity = int(quantity);
        if quantity > 0:
            break
    quantity = input("You entered a wrong number, please re-enter the quantity: \n")

subtotal = price * quantity
# GST = subtotal* constant.GST_rate;
# QST = (subtotal + GST) * constant.QST_rate;
GST = subtotal* GST_rate;
QST = (subtotal + GST) * QST_rate;
total_price = subtotal + GST + QST;




print("Product price: $", "%.2f" % price);
print("Quantity:", quantity,"\n");
print("Subtotal: $", "%.2f" %subtotal);
print("GST: $", "%.2f" %GST);
print("QST: $", "%.2f" %QST);
print("Total Price: $", "%.2f" %total_price);

print("\n===========================\n")


#3 –	Make a program that calculates an employee’s gross salary for a week, 
#      given their hourly rate and the number of hours worked. 


rate = input("Please enter your hourly rate: \n")
while True:
    if is_number(rate) == True:
        rate = float(rate); 
        if price > 0:
            break
    rate = input("You entered a wrong number, please re-enter your rate: \n") 
    
hour = input("Please enter the hours: \n")
while True:
    if hour.isdigit() == True :
        hour = int(hour);
        if hour > 0:
            break
    hour = input("You entered a wrong number, please re-enter the hour: \n")
    
salary = rate * hour 
print("the salary is : $","%.2f" %salary)

print("\n===========================\n")

#4 	Make a program that reads a temperature in degrees Fahrenheit and 
#   converts it into degrees Celsius. The conversion formula is:

#   C=  (F-32)/9  ×5


F = input("Please enter the Fahrenheit: \n")
while True:
    if F.isdigit() == True :
        F = int(F);
        if F > 0:
            break
    F = input("You entered a wrong number, please re-enter the Fahrenheit: \n")

C = (F - 32) / 9 * 5

print("Celsius is : $","%.2f" %C)

print("\n===========================\n")

# 5 – Make a program that displays the volume of a rectangular prism 
#     after reading the dimensions of the prism.


length = input("Please enter the length: \n")
while True:
    if is_number(length) == True:
        length = float(length); 
        if length > 0:
            break
    length = input("You entered a wrong number, please re-enter the length: \n")

width = input("Please enter the width: \n")
while True:
    if is_number(width) == True:
        width = float(width); 
        if width > 0:
            break
    width = input("You entered a wrong number, please re-enter the width: \n")
    
height = input("Please enter the height: \n")
while True:
    if is_number(height) == True:
        height = float(height); 
        if height > 0:
            break
    height = input("You entered a wrong number, please re-enter the height: \n")

volume = length * width * height;


print("The volume of rectangular prism is: \n", volume);

print("\n===========================\n")



# 6 – A dealership selling new vehicles asks you to construct a program 
#     that calculates the compensation paid to their salespeople. 
#     The base salary for all the salespeople is $400. 
#     For each vehicle sold, the salesperson receives a commission of $200. 
#     Also, the salesperson receives a bonus of 5% of the total amount of all their sales.
#     Make the program for a salesperson.


vehicle_sold = input("How many vehicle were sold? \n")
    
while True:
    if vehicle_sold.isdigit() == True :
        vehicle_sold = int(vehicle_sold);
        if vehicle_sold >= 0:
            break
    vehicle_sold = input("You entered a wrong number, please re-enter the quantity: \n")

if vehicle_sold == 0:
    amount = 0;
else:
    amount = input("what's the total amount of your sales? \n")
    while True:
        if is_number(amount) == True:
            amount = float(amount); 
            if amount > 0:
                break
        amount = input("You entered a wrong number, please re-enter the amount: \n")

commission = 200 * vehicle_sold;
bonus = amount * 0.05;

total_salary = 400 + commission + bonus;

print("Base salary: $ 400.00");
print("Commission: $", "%.2f" %commission);
print("Bonus: $", "%.2f" %bonus);
print("Total salary: $", "%.2f" %total_salary);