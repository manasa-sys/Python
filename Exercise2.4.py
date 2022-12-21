#program that calculates the final grade of a student,
# assuming that each of the three grades the user inputs is out of 100
#Enter the laboratory marks out of 100
lab_marks=input('Please enter your lab marks: ')
lab_marks = float(lab_marks)
while(True):
    if(lab_marks>0):
        break
    print('invalid marks..please enter a valid mark between(0-100): ')
    lab_marks=input('Please enter your lab marks: ')
    lab_marks = float(lab_marks)
#Enter the midterm marks out of 100
midterm_marks=input('Please enter your mid-tem marks  : ')
midterm_marks = float(midterm_marks)
while(True):
    if(midterm_marks>0):
        break
    print('invalid marks..please enter a valid mark between (0-100): ')
    midterm_marks=input('Please enter your midterm marks ')
    midterm_marks = float(midterm_marks)

#Enter the final marks out of 100
final_marks=input('Please enter your final marks: ')
final_marks = float(final_marks)
while(True):
    if(final_marks>0):
        break
    print('invalid marks..please enter a valid mark between (0-100): ')
    final_marks=input('Please enter your final marks: ')
    final_marks = float(final_marks)
#diaplying the entered marks
print('lab marks : '+ str(lab_marks))
print('midterm marks: '+ str(midterm_marks))
print('final_marks: '+ str(final_marks))
# caluculating the final grade
final_grade= float((0.4*lab_marks)+(0.25*midterm_marks) +(0.35*final_marks))
print('final grade of the student is: '+ str(final_grade))
