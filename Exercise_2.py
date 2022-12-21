#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment_1 
Exercise_2

Created on Mon Sep  5 00:00:59 2022

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

# 2 – We want to determine the height of a building of n floors, 
#     knowing that the ground floor has a height of 6 meters 
#     and that the other floors each have a height of 4 meters.

n = input("How many floors does this building have？ \n");

while True:
    if n.isdigit() == True:
        n = int(n);
        if n > 0:
            break
    else:
        n = input("You entered a wrong number, please re-enter an integer: \n");

height1 = 6 + 4 * (n);
print("Ground floor as the ground floor:")
print("The height of the ground floor and {} floors is {}" .format(n,height1), "m \n");

height2 = 6 + 4 * (n-1);
print("Ground floor as the first floor:")
print("The height of the ground floor and {} floors is {}" .format(n-1,height2), "m \n");

print("\n===========================\n")




# 3 – An aircraft pilot wants to know the atmospheric pressure, 
#     expressed in atmosphere units (atm), 
#     as the weather station only provides pressure data in kilopascal units (kPa).
#     1 atm is equivalent to 101.325 kPa. Make a program that performs the conversion.


kPa = input("Please enter kPa: \n");

while True:
    if is_number(kPa) == True:
        kPa = float(kPa); 
        if kPa > 0:
            break
    kPa = input("You entered a wrong number, please re-enter the kPa: \n")

atm = kPa/101.325

print(kPa, "kPa =", atm,"atm");

print("\n===========================\n")


# 4 – In a computer technology course, the following evaluation weights are used:

# •	Laboratory work counts for 40% of the grade
# •	The midterm exam counts for 25%
# •	The final exam counts for 35%

# Make a program that calculates the final grade of a student, 
# assuming that each of the three grades the user inputs is out of 100.


lab = input("Please enter the grade of lab: \n")
while True:
    if is_number(lab) == True:
        lab = float(lab); 
        if 100 >= lab >= 0:
            break
    lab = input("You entered a wrong number, please re-enter the grade of lab: \n")

midterm = input("Please enter the grade of midterm: \n")
while True:
    if is_number(midterm) == True:
        midterm = float(midterm); 
        if 100 >= lab >= 0:
            break
    midterm = input("You entered a wrong number, please re-enter the grade of midterm: \n")
    
final= input("Please enter the grade of final: \n")
while True:
    if is_number(final) == True:
        final = float(final); 
        if 100 >= lab >= 0:
            break
    final = input("You entered a wrong number, please re-enter the grade of final: \n")

overall = lab * 0.4 + midterm * 0.25 + final * 0.35;

print("The overall grade is: ", overall);

print("\n===========================\n")


# 5 –	Monique want to have a little program that allows her to evaluate 
#     the total amount of her expenses for a month, 
#     as well as the amount of money she can allocate for her leisure activities 
#     and non-essential spending. 
#     The program should read her projections for expenses in the following categories:

# Weekly expenses (one time per week; assuming that 1 month = 4 weeks)
# •	Food expenses and household expenses
# •	Common expenses

# Monthly expenses (one time per month)
# •	Public transit pass
# •	Rent
# •	Total of monthly bills

# The program should also read the amount of her paycheques. Monique receives two paycheques per month.

# The program should then display her total expenses, her total income, and the difference.

paycheque1 = input("Please enter the amount of your first paycheque: \n")
while True:
    if is_number(paycheque1) == True:
        paycheque1 = float(paycheque1); 
        if paycheque1 >= 0:
            break
    paycheque1 = input("You entered a wrong number, please re-enter the amount of your first paycheque: \n")

paycheque2 = input("Please enter the amount of your second paycheque: \n")
while True:
    if is_number(paycheque2) == True:
        paycheque2 = float(paycheque2); 
        if paycheque2 >= 0:
            break
    paycheque2 = input("You entered a wrong number, please re-enter the amount of your second paycheque: \n")
    
food_household = input("Please enter the expenses of your Food and household for each week\n")
while True:
    if is_number(food_household) == True:
        food_household = float(food_household); 
        if food_household >= 0:
            break
    food_household = input("You entered a wrong number, please re-enter the expenses of your Food and household for each week: \n")    
    
common = input("Please enter your common expenses for each week\n")
while True:
    if is_number(common) == True:
        common = float(common); 
        if common >= 0:
            break
    common = input("You entered a wrong number, please re-enter your common expenses for each week: \n")        
    
transit = input("Please enter your expense of public transit pass for each month\n")
while True:
    if is_number(transit) == True:
        transit = float(transit); 
        if transit >= 0:
            break
    transit = input("You entered a wrong number, please re-enter your expense of public transit pass for each month: \n")            
    
rent = input("Please enter your expense of rent for each month\n")
while True:
    if is_number(rent) == True:
        rent = float(rent); 
        if rent >= 0:
            break
    rent = input("You entered a wrong number, please re-enter your expense of rent for each month: \n")     
    
bill = input("Please enter your Total of monthly bills\n")
while True:
    if is_number(bill) == True:
        bill = float(bill); 
        if bill >= 0:
            break
    bill = input("You entered a wrong number, please re-enter your Total of monthly bills: \n")     
    
totalexpenses = (food_household + common) * 4 + transit + rent + bill    

totalincome = paycheque1 + paycheque2

difference = totalincome - totalexpenses
    
print("The total expenses is $", "%.2f" %totalexpenses);
print("The total income is $", "%.2f" %totalincome);
print("The balance is $", "%.2f" %difference);