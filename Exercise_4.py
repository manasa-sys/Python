#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment_1 
Exercise_4

Created on Sun Sep  5 00:34:30 2022

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


#24 –	In a game, the player tosses two coins. Let’s suppose that,
#       if the first and second coin land on heads, the player wins $10;
#       if the first lands on heads and the second on tails, the player wins $5;
#       otherwise, the player loses.
#       We want a program that reads the value of the two coins (heads or tails)
#       and determines whether the player has won. If yes, it should display the amount won.


m = input("what's your first lands: 1. head  2. tail \n")    
while True:
    if m.isdigit() == True :
        m = int(m);
        if 2 >= m >= 1:
            break
    m = input("You entered a wrong number, please re-enter an integer: \n")

n = input("what's your second lands: 1. head  2. tail \n")    
while True:
    if n.isdigit() == True :
        n = int(n);
        if 2 >= m >= 1:
            break
    n = input("You entered a wrong number, please re-enter the other integer: \n")
    
if m == 1 and n == 1:
    print("You win $10")
elif (m == 1 and n == 2) or (m == 2 and n == 1):
    print("You win $5\n")
else:
    print("You lose, try it again\n")
    
print("\n===========================\n")
    
#25 –	Write a program that reads 3 values, determines the greatest one, and displays it.


a = input("Please enter the first number: \n")
while True:
    if is_number(a) == True:
        a = float(a)
        break
    a = input("You entered a wrong number, please re-enter the first number: \n")

b = input("Please enter the second number: \n")
while True:
    if is_number(b) == True:
        b = float(b)
        break
    b = input("You entered a wrong number, please re-enter the second number: \n")

if a > b:
    x = a;
else:
    x = b;
    
c = input("Please enter the third number: \n")
while True:
    if is_number(c) == True:
        c = float(c)
        break
    c = input("You entered a wrong number, please re-enter the third number: \n")
    
if c > x:
    print("{} is the greatest number\n".format(c))
else:
    print("{} is the greatest number\n".format(x)) 

print("\n===========================\n")



#26 –	Write a program that reads three values and displays them in ascending order. 
   
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
    
if a >= b >= c:
    print(c,b,a)
elif a >= c >= b:
    print(b,c,a) 
elif b >= a >= c:
    print(c,a,b)
elif b >= c >= a:
    print(a,c,b)
elif c >= a >= b:
    print(b,a,c)
elif c >= b >= a:
    print(a,b,c)    

print("\n===========================\n")
    
# 27 –	The Ministère des Finances of Québec is adopting a project aiming to reduce taxes. 
#         Develop an algorithm that calculates taxes according to the table provided below. 
#         In addition, a 2% reduction of the tax rate is granted if the person is married. 
#         Furthermore, a 0.5% reduction is granted for each child. 
#         Finally, 8% is subtracted from the tax rate for those who have newly arrived in the province.
#         Determine the amount of tax to be paid as a function of the information provided by the user. 
 
#  	Table of basic tax rates:
 
#        Salary                    	Tax rate
#  $0.00 to $18,000.00 	              10% 
#  $18,000.01 to $32,000.00           20% 
#  $32,000.01 to $60,000.00 	      30% 
#  $60,000.01 and more	              40% 


salary = input("Please enter your salary: \n")
while True:
    if is_number(salary) == True:
        salary = float(salary); 
        if salary >= 0:
            break
    salary = input("You entered a wrong number, please re-enter your salary: \n")

if 0 <= salary <= 18000:
    rate = 0.1
elif 18000.01 <= salary <= 32000:
    rate = 0.2
elif 32000.01 <= salary <= 60000:
    rate = 0.3
else:
    rate = 0.4
    
married = input("Are you married? (Y/N) \n")
if married == "Y" or married == "y":
    rate -= 0.02

child = input("How many children do you have ? \n")
while True:
    if child.isdigit() == True :
        child = int(child);
        if child >= 0:
            break
    child = input("You entered a wrong number, How many children do you have?: \n")

rate -= child * 0.005

new_arrival= input("Are you new arrival? (Y/N) \n")
if new_arrival == "Y" or new_arrival == "y":
    rate -= 0.08

if rate < 0:
    rate = 0

tax = salary * rate

print("Tax: $","%.2f" %tax)