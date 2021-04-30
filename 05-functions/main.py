

def average(data):
	return sum(data) / len(data)


def minimum(data):
	return min(data)


def maximum(data):
	return max(data)


def data_range(data):
	return minimum(data), maximum(data)


def median(data):
	sorted_data = sorted(data)
	data_length = len(data)
	index = (data_length - 1) // 2

	if data_length % 2:
		return sorted_data[index]
	else:
		return (sorted_data[index] + sorted_data[index + 1]) / 2.0


def celsius_to_fahrenheit(celsius):
	return (celsius * 9/5) + 32


def main():
	# Set up the data the data file
	readings = [13.5, 12.6, 15.3, 12.2, 16.6, 14.6, 15.6]

	# Find minimum, maximum etc in readings
	print('Min temp in list =', minimum(readings))
	print('Max temp in list =', maximum(readings))
	print('Average temperature = {:.2f}'.format(average(readings)))
	print('Median temperature value =', median(readings))
	readings_range = data_range(readings)
	print('Range of temperatures from ', str(readings_range[0]) + ' to ' + str(readings_range[1]))

	print('13.5 celsius as fahrenheit -', celsius_to_fahrenheit(13.5))

	print('Done')


if __name__ == '__main__':
	main()