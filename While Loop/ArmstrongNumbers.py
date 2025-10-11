num = int(input('Enter the number'))
sum = 0
i = num
while i > 0:
    digit = i % 10
    sum = sum + digit ** 3
    i = i // 10
if num == sum:
    print(num, 'Is an Armstrong number')
else:
    print(num, 'Is not an Armstrong number')