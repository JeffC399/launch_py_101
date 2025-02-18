def is_it_odd(number):
    print(False if abs(number) % 2 == 0 else True)

my_number = int(input("Enter a number: "))

is_it_odd(my_number)