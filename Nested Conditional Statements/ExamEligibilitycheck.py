medicalCert = input('Do you have a medical certificate for the exam : (yes/no)')
if medicalCert =='yes':
    attendence = int(input("Enter the attendance of the student : "))
    if attendence >= 75:
        print('You are allowed for the exam')
    else:
        print('You are not allowed for the exam')
else:
    print('You are not eligible for the exam')