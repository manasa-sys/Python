
#program that reads the unit price of a product and the quantity purchased,
# and that displays the amounts for the GST, the QST, and the total price after taxes.
# GST,QST calculation
price=(input('Enter the unit price: '))
price=float(price)
unit=(input('Enter the number of units: '))
unit=int(unit)
totalprice=float(price*unit)
print('Total price is '+ str(totalprice))
#to calculate gst
gst=float(0.07*totalprice)
print('GST is '+str(gst))
#totalprice after gst
tot_afgst=float(gst+totalprice)
print('Total price after gst is '+str(tot_afgst))
#to calculate qst
qst=float(tot_afgst*0.075)
print('QST is '+str(qst))
#total price after tax
totalaftax=float(totalprice+gst+qst)
print('Total amount after tax is '+str(totalaftax))

