#while loop keeps going on positive value inputs
# but stops w/ negative value


print('')

print('STAY POSITIVE!')
print('')
print('(hint: enter a few positive values\n'
      'then see what happens with a negative value.')

print('')
z = float(input('Enter numeric value: '))

while z >= 0:
    print(f"Yes, {z} works.")
    print('')
    z = float(input('Enter another value: '))
    print('')
print('Nope, no negativity! The End.')

print('')

