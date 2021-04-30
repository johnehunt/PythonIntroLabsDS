from readings import TemperatureReading
from utils import *


def main():

	# Set up the data the data file
	readings = [
			TemperatureReading(13.5, '01/05/20', 'London', 'Celsius'),
			TemperatureReading(12.6, '02/05/20', 'London', 'Celsius'),
			TemperatureReading(15.3, '03/05/20', 'London', 'Celsius'),
			TemperatureReading(12.2, '04/05/20', 'London', 'Celsius'),
			TemperatureReading(16.6, '05/05/20', 'London', 'Celsius'),
			TemperatureReading(14.6, '05/05/20', 'London', 'Celsius'),
			TemperatureReading(15.6, '05/05/20', 'London', 'Celsius')
	]

	# Obtain just the temperatures, dates and the indexes for each value
	temperatures = list(map(lambda r: r.value, readings))
	print('Temperatures:', temperatures)
	dates = list(map(lambda r: r.date, readings))
	print('Dates:', dates)

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

	print('Done')


if __name__ == '__main__':
	main()
