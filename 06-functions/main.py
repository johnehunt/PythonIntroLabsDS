# Example illustrating defining and invoking functions

def average(data):
	return sum(data) / len(data)


def median(data):
	sorted_data = sorted(data)
	data_length = len(data)
	index = (data_length - 1) // 2

	if data_length % 2:
		return sorted_data[index]
	else:
		return (sorted_data[index] +
		        sorted_data[index + 1]) / 2.0


def minimum(data, index=0):
	if index == 0:
		data_slice = data
	else:
		data_slice = data[index:]
	return min(data_slice)


def maximum(data, index=0):
	if index == 0:
		data_slice = data
	else:
		data_slice = data[index:]
	return max(data_slice)


def data_range(data):
	return minimum(data), maximum(data)


def celsius_to_fahrenheit(celsius):
	return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
	return (fahrenheit - 32) * 5 / 9


# Set up the readings to process
readings = [13.5, 11.1, 17.5, 12.6, 15.3, 12.2, 16.6, 14.6]

# Find the average and median values
print('Average temperature = {:.2f}'.format(average(readings)))
print(f'Median temperature value = {median(readings)}')

# Find minimum, maximum etc in readings
print(f'Min temp in list = {minimum(readings)}')
print(f'Min temp in list start position 4 = {minimum(readings, 3)}')
print(f'Max temp in list = {maximum(readings)}')
print(f'Max temp in list starting position 4 = {maximum(readings, 3)}')

readings_range = data_range(readings)
print('Range of temperatures from ', str(readings_range[0]) + ' to ' + str(readings_range[1]))

print('13.5 celsius as fahrenheit -', celsius_to_fahrenheit(13.5))

print('Done')
