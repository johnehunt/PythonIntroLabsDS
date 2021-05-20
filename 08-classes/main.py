class TemperatureReading:
	""" Specialised version of Reading to incorporates temperature info """

	def __init__(self, temp, date, location, scale):
		self.temp = temp
		self.date = date
		self.location = location
		self.scale = scale

	def temp(self):
		return self.temp

	def __str__(self):
		return 'TemperatureReading[' + self.scale + '](' + str(self.temp) + ' on ' + str(self.date) + ' at ' + str(
				self.location) + ')'


def average(data):
	if isinstance(data[0], int):
		return sum(data) / len(data)
	else:
		raw_data = list(map(lambda r: r.temp, data))
		return sum(raw_data) / len(raw_data)


def minimum(data):
	result = None
	for item in data:
		if result is None:
			result = item
		elif result.temp > item.temp:
			result = item
	return result


def maximum(data):
	result = None
	for item in data:
		if result is None:
			result = item
		elif result.temp < item.temp:
			result = item
	return result


def data_range(data):
	return minimum(data), maximum(data)


def bubble_sort(data):
	data_list = list(data)
	pass_number = 0
	for i in range(len(data_list) - 1, 0, -1):
		exchanges = False
		pass_number += 1
		for j in range(0, i):
			if data_list[j].temp > data_list[j + 1].temp:
				exchanges = True
				temp = data_list[j]
				data_list[j] = data_list[j + 1]
				data_list[j + 1] = temp
		if not exchanges:
			break
	return data_list


def median(data):
	sorted_data = bubble_sort(data)
	data_length = len(data)
	index = (data_length - 1) // 2

	if data_length % 2:
		return sorted_data[index]
	else:
		return (sorted_data[index] + sorted_data[index + 1]) / 2.0


def celsius_to_fahrenheit(celsius):
	return (celsius * 9 / 5) + 32


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

	# Convert all the temperatures from Celsius to fahrenheit
	fahrenheit_temperatures = list(map(lambda r: celsius_to_fahrenheit(r.temp), readings))
	print('Fahrenheit Temperatures:', fahrenheit_temperatures)

	# Obtain just the temperatures, dates and the indexes for each value
	temperatures = list(map(lambda r: r.temp, readings))
	print('Temperatures:', temperatures)
	dates = list(map(lambda r: r.date, readings))
	print('Dates:', dates)

	# Find all temperatures above 14.0
	higher_temperatures = list(filter(lambda r: r.temp > 14.0, readings))
	print('Temperatures above 14.0:', higher_temperatures)

	# Find minimum, maximum etc in readings
	print('Min temp in list =', minimum(readings))
	print('Max temp in list =', maximum(readings))
	print('Average temperature = {:.2f}'.format(average(readings)))
	print('Median temperature value =', median(readings))
	readings_range = data_range(readings)
	print('Range of temperatures from ', str(readings_range[0].temp) + ' to ' + str(readings_range[1].temp))

	print('Done')


if __name__ == '__main__':
	main()
