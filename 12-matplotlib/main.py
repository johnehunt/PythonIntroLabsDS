import matplotlib.pyplot as pyplot

from loader import load_data
from utils import *


def main():

	# Load the data file
	readings = load_data('data.csv')
	for reading in readings:
		print(reading)
	dates = list(map(lambda r: r.date, readings))
	temperatures = list(map(lambda r: r.temp(), readings))
	index = range(len(readings))

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
