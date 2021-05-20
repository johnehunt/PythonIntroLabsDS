readings = []

while True:
	input_string = input('Please enter a temperature reading (-1 to end): ')
	if input_string == '-1':
		break
	elif not input_string.replace(".", "").isdigit():
		print('Must be a positive number')
	else:
		reading = float(input_string)
		readings.append(reading)

print('Temperature readings input:', readings)

readings.sort()
print('Temperature readings sorted:', readings)

readings.reverse()
print('Temperature readings in reverse:', readings)
