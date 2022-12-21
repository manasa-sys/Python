# Temperature in degree fahrenhiet
#program that reads a temperature in degrees Fahrenheit and converts it into degrees Celsius.
deg_f=(input('enter the temperature in degree Fahrenheit: '))
deg_f=float(deg_f)

#Temperature in degree celsius
deg_c=float(((deg_f-32)/9)*5)
print('Temperature in degree celcius is '+ str(deg_c))