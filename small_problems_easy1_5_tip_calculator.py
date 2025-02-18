bill = float(input('Enter the amount of your bill: '))
tip_percentage = float(input('Enter your tip percentage: '))

total_tip = bill * (tip_percentage / 100)
total_amount = bill + total_tip

print(f'The tip is ${total_tip:.2f}')
print(f'The total is ${total_amount:.2f}')