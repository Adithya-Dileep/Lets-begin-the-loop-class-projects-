print("Select your ride \n 1. Bike \n 2. Car")
vehicle = int(input("Enter your choice : "))
if vehicle == 1:
    print("You have selecte the Bike")
    print("Enter the type of Bike \n b1. Hero Splendor \n b2. Honda Shine")
    bike = input("Enter the choice of bike : ")
    if bike == 'b1':
        print("you have selected Hero Splendor")
    else:
        print("you have selectedHonda Shine ")
elif vehicle == 2:
    print("You have selecte the Car")
    print("Enter the type of Car \n c1. Indica \n c2. Xylo ")
    car = input("Enter the choice of car : ")
    if car == "c1":
        print("you have selected Indica")
    else:
        print("you have selected Xylo")