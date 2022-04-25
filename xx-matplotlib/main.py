import matplotlib.pyplot as pyplot

from loader import load_data
from readings import TemperatureReading
from readings import RainfallReading
from readings import InvalidTemperatureException
from utils import *


def main():
	# Load the data file
	readings = load_data('data.csv')

	print('All Temperature Readings:')
	print(*readings, sep=", ")

	# Convert all the temperatures from Celsius to fahrenheit
	fahrenheit_temperatures = list(map(lambda r: celsius_to_fahrenheit(r.value), readings))
	print('Fahrenheit Temperatures:', fahrenheit_temperatures)

	# Find all temperatures above 14.0
	higher_temperatures = list(filter(lambda r: r.value > 14.0, readings))
	print('Temperatures above 14.0:', higher_temperatures)

	# Find minimum, maximum etc in readings
	print('Min temp in list =', minimum(readings))
	print('Max temp in list =', maximum(readings))
	print('Average temperature = {:.2f}'.format(average(readings)))
	print('Median temperature value =', median(readings))
	readings_range = data_range(readings)
	print('Range of temperatures from ', str(readings_range[0].value) + ' to ' + str(readings_range[1].value))

	# Add temperatures together
	new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + TemperatureReading(15.5, '01/05/20',
	                                                                                                 'London',
	                                                                                                 'Celsius')
	print('Add two temperatures', new_temperature)

	new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5
	print('Add a temperature and a int', new_temperature)

	new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5.5
	print('Add a temperature and a float', new_temperature)

	# Working with Rainfall readings
	rainfall_readings = [
			RainfallReading(2.0, '01/05/20', '11:00', 'London'),
			RainfallReading(2.6, '02/05/20', '11:30', 'London'),
			RainfallReading(2.3, '03/05/20', '11:00', 'London'),
			RainfallReading(3.2, '04/05/20', '12:00', 'London'),
			RainfallReading(1.6, '05/05/20', '10:45', 'London')
	]

	print('All Rainfall Readings:')
	print(*rainfall_readings, sep=", ")
	print(f'Average rainfall {average(rainfall_readings)}')

	try:
		new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + '5.5'
	except InvalidTemperatureException as e:
		print(e)

	# Obtain just the temperatures, dates and the indexes for each value
	temperatures = list(map(lambda r: r.value, readings))
	print('Temperatures:', temperatures)
	dates = list(map(lambda r: r.date, readings))
	print('Dates:', dates)
	# Generate a range for the indexes of the bar chart
	index = range(len(readings))

	# Set the size of the graph
	pyplot.figure(figsize=(10, 8))

	# Set up the bar chart
	pyplot.bar(index, temperatures, tick_label=dates)
	pyplot.xticks(rotation=750)

	pyplot.ylabel('Temperature')
	pyplot.xlabel('Dates')

	# Display the chart
	pyplot.show()

	print('Done')


if __name__ == '__main__':
	main()
