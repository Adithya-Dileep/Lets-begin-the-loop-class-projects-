# Program to check if a number is prime or not
num = int(input("Enter the number : "))
# define a flag variable
flag = False
if num == 0 or num == 1:
    print(num, "is a composite number")
elif num > 1:
# check for factors
    for i in range(2, num):
        if (num % i) == 0:
# if factor is found, set flag to True
            flag = True
# break out of loop
            break
# check if flag is True
    if flag == True:
        print(num, "is a composite number")
    else:
        print(num, "is a prime number")