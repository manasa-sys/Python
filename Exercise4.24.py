pos_1=input('please enter the first landing(H/T): ')
pos_2=input('please enter the second landing(H/T): ')
if(pos_1=='H' and pos_2=='H') :
    winAmount= 10;
    print('Amount won is:'+str(winAmount) + '$')
elif(pos_1=='h' and pos_2=='h') :
    winAmount= 10;
    print('Amount won is:'+str(winAmount) + '$')
elif(pos_1=='H' and pos_2=='T') :
    winAmount= 5;
    print('Amount won is:'+str(winAmount) + '$')
elif(pos_1=='h' and pos_2=='t') :
    winAmount= 5;
    print('Amount won is:'+str(winAmount) + '$')
else:
    print('Lost game ,please try again')
