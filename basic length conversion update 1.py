number = 0.0
FEET_TO_METERS = .3048
METERS_TO_KILOMETERS = .001
METERS_TO_CENTIMETERS = 100.0
METERS_TO_MILIMETERS = 1000.0
FEET_TO_INCHES = 12.0
YARDS_TO_FEET = 3.0
answer = 0.0

converting_from = input('Enter the unit abbreviation you wish to convert from: ')
converting_to = input('Enter the unit abbreviation you wish to convert to: ')
number = input('What is the value that needs converted? ')

while( converting_from != converting_to )
	if(converting_from == 'ft')
		if(converting_to == 'in')
			answer = number * FEET_TO_INCHES
			converting_from = 'in'
		else if(converting_to == 'yd')
			answer = number / YARDS_TO_FEET
			converting_from = 'yd'
		else if(converting_to == 'mm' or 'cm' or 'm' or 'km')
			number = number * FEET_TO_METERS
			converting_from = 'm'
	else if(converting_from == 'in')
		if(converting_to == 'yd' or 'ft' or 'mm' or 'cm' or 'm' or 'km')
			number = number / FEET_TO_INCHES
			converting_from = 'ft'
	else if(converting_from == 'yd')
		if(converting_to == 'ft' or 'in' or 'mm' or 'cm' or 'm' or 'km')
			number = number * YARDS_TO_FEET
			converting_from = 'ft'
	else if(converting_from == 'm')
		if(converting_to == 'ft' or 'in' or 'yd')
			number = number / FEET_TO_METERS
			converting_from = 'ft'
		else if(converting_to == 'mm')
			answer = number * METERS_TO_MILIMETERS
			converting_from = 'mm'
		else if(converting_to == 'cm')
			answer = number * METERS_TO_CENTIMETERS
			converting_from = 'cm'
		else if(converting_to == 'km')
			answer = number * METERS_TO_KILOMETERS
			converting_from = 'km'
	else if(converting_from == 'mm')
		if(coverting_to == 'in' or 'ft' or 'yd' or 'cm' or 'm' or 'km')
			number = number / METERS_TO_MILIMETERS
			converting_from = 'm'
	else if(converting_from == 'cm')
		if(converting_to == 'in' or 'ft' or 'yd' or 'cm' or 'm' or 'km')
			number = number / METERS_TO_CENTIMETERS
			converting_from = 'm'
	else if(converting_from == 'km')
		if(converting_to == 'in' or 'ft' or 'yd' or 'cm' or 'm' or 'km')
			number = number / METERS_TO_KILOMETERS
			converting_from = 'm'
print(answer converting_to)
				
		
