#Enter the pressure in kPa
pressure_kpa=float(input('enter the pressure in kpa: '))
while(True):
    if(pressure_kpa>=0):
        break
    print('enter a valid pressure: ')
    pressure_kpa=float(input('enter the pressure in kpa: '))
#pressure in kPa is converted to atm using the following formula
pressure_atm=float(pressure_kpa/101.325)
print('Pressure in atm is :'+ str(pressure_atm))

