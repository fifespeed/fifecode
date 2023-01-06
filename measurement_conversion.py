
print('')
print('')
print('')
print('')
print('')

print('MEASUREMENT CONVERSION TOOL')
print('____________________________')

print('')
print('Convert inches to centimeters,\n'
      'or centimeters to inches.\n' 
      'For starting values in inches, enter "i".\n'
      'For starting values in centimeters, enter "c".')
print('')
print('____________________________')

convert_value = 2.54

print('')

convert_choice = str(input('Enter i or c: '))

print('')

measure = float(input('Enter measurement: '))

print('')


if convert_choice == "c":
    v = float((measure / convert_value))
    print(f"{measure} centimeters is {v} inches.")
     
else:
    v = float((measure * convert_value))
    print(f"{measure} inches is {v} centimeters.")


print('')
print('')
print('')
