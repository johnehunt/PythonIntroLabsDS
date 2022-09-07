# Illustrates use of higher order functions such as filter, map and reduce
from functools import reduce


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
	return (fahrenheit - 32) * 5/9


# Set up the data the data file
readings = [13.5, 12.6, 15.3, 12.2, 16.6, 14.6, 15.6]

print(f'Readings: {readings}')

# Find minimum, maximum etc in readings
print('Min temp in list =', minimum(readings))
print('Max temp in list =', maximum(readings))
print('Average temperature = {:.2f}'.format(average(readings)))
print('Median temperature value =', median(readings))
readings_range = data_range(readings)
print(f'Range of temperatures from {readings_range[0]} to {readings_range[1]}')

# Convert all the temperatures from Celsius to fahrenheit
fahrenheit_temperatures = list(map(celsius_to_fahrenheit, readings))
print(f'Fahrenheit Temperatures: {fahrenheit_temperatures}')

# Find all temperatures above 14.0
higher_temperatures = list(filter(lambda r: r > 14.0, readings))
print(f'Temperatures above 14.0: {higher_temperatures}')

# Total all the readings
total_of_readings = sum(readings)
print(f'Total of all readings = {total_of_readings}')

# Total of all readings using reduce
result = reduce(lambda total, value: total + value, readings)
print(f'Total value of all readings is {result}')

# Convert all readings above 14.0 to fahrenheit
converted_temperatures = list(map(celsius_to_fahrenheit, filter(lambda r: r > 15.5, readings)))
print(f'Fahrenheit Temperatures above 14.0c: {converted_temperatures}')

print('Done')

