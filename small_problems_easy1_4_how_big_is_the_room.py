# length = float(input('Enter the length of the room (in meters): '))
# width = float(input('Enter the width of the room (in meters): '))

# area_in_square_meters = length * width
# area_in_square_feet = area_in_square_meters * 10.7639

# print(f'The room is {area_in_square_meters:.2f} '
#       f'square meters, and {area_in_square_feet:.2f} square feet!')

length = float(input('Enter the length of the room: '))
width = float(input('Enter the width of the room: '))

area = length * width

my_choice = input('Did you measure the room in meters or feet? ')
if my_choice == 'meters':
    not_my_choice = 'feet'
    area_in_other = area * 10.7639
else:
    not_my_choice = 'meters'
    area_in_other = area / 10.7639

print(f'The room\'s area is {area:.2f} square {my_choice} (or '
      f'{area_in_other:.2f} square {not_my_choice})!')