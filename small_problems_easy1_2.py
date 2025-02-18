# x = 1

# while(x <= 99):
#     if(x % 2 != 0):
#         print(x)
#     x += 1

starting_number = int(input('Enter the starting number :'))
ending_number = int(input('Enter the ending number: '))

for number in range(starting_number, ending_number + 1):
    if(number % 2 != 0):
        print(number)