rows = int(input("Enter number of rows: "))
for i in range(rows):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num + 1
    print("")