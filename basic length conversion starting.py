FEET_TO_CENTIMETERS = 30.48
FEET_TO_METERS = .3048
METERS_TO_KILOMETERS = 1000
METERS_TO_CENTIMETERS = .01
METERS_TO_MILIMETERS = .001
INCHES_TO_FEET = 12
INCHES_TO_YARDS = 36
FEET_TO_YARDS = 3
answer = 0

converting_from = input('Enter the unit you wish to convert from: ')
converting_to = input('Enter the unit you wish to convert to: ')
number = input('What is the value that needs converted? ')
if converting_from = inches

else if converting_from = feet
	if converting_to = yards
		answer = number * FEET_TO_YARDS
	else if converting_to = inches
		answer = number /INCHES_TO_FEET
	else if converting_to = centimeters
		answer = number * FEET_TO_CENTIMETERS
	else if converting_to = milimeters
		answer = number * FEET_TO_METERS * METERS_TO_MILIMETERS
	else if converting_to = meters
		answer = number * FEET_TO_METERS
	else if converting_to = kilometers
		answer = number * FEET_TO_METERS * METERS_TO_KILOMETERS
else if converting_from = yards

else if converting_from = milimeters

else if converting_from = centimeters

else if converting_from = meters

else if converting_from = kilometers

else	
	print "That is not a valid unit."
