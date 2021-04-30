from loader import load_data
from utils import *


def main():

	# Load the data file
	readings = load_data('data.csv')
	for reading in readings:
		print(reading)
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
