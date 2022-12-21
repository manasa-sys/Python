no_floors=int(input('please enter the number of floors: '))
height_grnd=6;
while(True):
    if(no_floors==0):
        print('totalheight :'+ str(height_grnd)+'m')
        break
    elif(no_floors>0):
        break
    print('please enter a valid number of floors: ')
    no_floors=int(input('please enter the number of floors: '))
    #to calculate the height of the building
height_nfloor= int(height_grnd+ no_floors*4)
print('Total height '+ str(height_nfloor)+ 'm')

