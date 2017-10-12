print('These are the supported units: seconds (s), minutes (min), hours (hr), and weeks (wk). Use the abbreviations.')

operation1 = str(input('Enter the initial unit: '))

operation2 = str(input('Enter desired unit conversion: '))

number_1 = int(input('Enter the initial number: '))


if operation1 == 's' and operation2 == 'min':
    print(str((number_1) / 60) + ' min')

elif operation1 == 's' and operation2 == 'hr':
    print(str(((number_1) / 60) / 60) + ' hr')

elif operation1 == 's' and operation2 == 'wk':
    print(str(((((number_1) / 60) / 60) / 24) / 7) + ' wk')
    
elif operation1 == 'min' and operation2 == 's':
    print(str(60 * number_1) + ' s')

elif operation1 == 'min' and operation2 == 'hr':
    print(str((number_1) / 60) + ' hr')

elif operation1 == 'min' and operation2 == 'wk':
    print(str((((number_1) / 60) / 24) / 7) + ' wk')

elif operation1 == 'hr' and operation2 == 's':
    print(str(number_1 * 60 * 60) + 's')

elif operation1 == 'hr' and operation2 == 'min':
    print(str(number_1 * 60) + 'min')

elif operation1 == 'hr' and operation2 == 'wk':
    print(str((number_1 / 24) / 7) + 'wk')

elif operation1 == 'wk' and operation2 == 's':
    print(str(number_1 * 7 * 24 * 60 * 60) + 's')

elif operation1 == 'wk' and operation2 == 'min':
    print(str(number_1 * 7 * 24 * 60) + 'min')

elif operation1 == 'wk' and operation2 == 'hr':
    print(str(number_1 * 7 * 24) + 'hr')

else:
    print('Error.')
