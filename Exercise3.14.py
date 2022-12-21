# #program to calculate the total bill
# no_of_copies=int(input('please enter the number of copies: '))
# #when the number of copies are less than 100
# if(no_of_copies<=100):
#     totalPrice= 0.05*no_of_copies
#     print('total price is '+str(totalPrice))
#
# #when the number of copies are more than 100
# else(no_of_copies>100):
#     totalPrice= 5+(no_of_copies-100)*0.03
#     print('total price is '+str(totalPrice))


Order_quantity = float(input("Enter the number of photocopy you would to get : "))
if Order_quantity <= 100 :
    Price = Order_quantity * 0.05
    print("Total Price: $ %f" % Price)
else:
    qty_above_100 = Order_quantity - 100
    Price = 5 + (qty_above_100 * 0.03)
    print("Total Price:$ %f" % Price)
