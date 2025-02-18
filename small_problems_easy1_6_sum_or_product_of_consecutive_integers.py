# ATTEMPT NO. 1 ...
# number = int(input('Please enter an integer greater than 0: '))
# choice = input('Enter "s" to compute the sum, or "p" to computer the product: ')

# if(choice == 's'):
#     result = 0
#     method = 'sum'
#     for number in range(1, number + 1):
#         result += number
# else:
#     result = 1
#     method = 'product'
#     for number in range(1, number + 1):
#         result *= number

# ATTEMPT NO. 2 ... 
# print(f'The {method} of the integers between 1 and {number} is {result}.')

# def get_number():
#     number = int(input('Please enter an integer greater then 0: '))
#     calculate_the_result(number)

# def calculate_the_result(number):
#     get_the_method = input('Enter "s" to compute the sum, or "p" to computer the product: ')

#     if get_the_method == 's':
#         result = 0
#         method = 'sum'
#         for item in range(1, number + 1):
#             result += item
#     else: 
#         result = 1
#         method = 'product'
#         for item in range(1, number + 1):
#             result *= item

#     print(f'The {method} of the integers between 1 and {number} is {result}.')

# get_number()

# ATTEMPT NO. 3 ...
# Program functions
def compute_sum(target_num):
    return sum(range(1, target_num+1))

def compute_product(target_num):
    result = 1
    for num in range(1, target_num+1):
        result *= num
    return result

# Obtain valid user input
prompt1 = "Please enter an integer greater than 0: "
prompt2 = ('Enter "s" to compute the sum, '
           'or "p" to compute the product:  ')

number = input(prompt1) 
while True:
    try: 
        int(number)
    except ValueError:
        number = input("Please enter an INTEGER: ")
    else:
        if int(number) > 0:
            break
        else:
            number = input("Please enter an integer GREATER THAN ZERO: ")

number = int(number)

operation = input(prompt2)
while operation not in ['s', 'p']:
    operation = input(prompt2)

# Print out the results
print()

if operation == "s":
    print(f'The sum of the integers between 1 and {number} is {compute_sum(number)}')
elif operation == "p":
    print(f'The product of the integers between 1 and {number} is {compute_product(number)}')