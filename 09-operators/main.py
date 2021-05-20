class TemperatureReading:
	""" Class representing temperature info.
	    It includes comparison operators
	    which allow temperatures to be compared as well as added and subtracted.
	"""

	def __init__(self, temp, date, location, scale):
		self.temp = temp
		self.date = date
		self.location = location
		self.scale = scale

	def __add__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			new_value = self.temp + other
		else:
			new_value = self.temp + other.temp
		return TemperatureReading(new_value, self.date, self.location, self.scale)

	def __sub__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			new_value = self.temp - other
		else:
			new_value = self.temp - other.temp
		return TemperatureReading(new_value, self.date, self.location, self.scale)

	def __eq__(self, other):
		return self.temp == other.temp

	def __ne__(self, other):
		return self.temp != other.temp

	def __ge__(self, other):
		return self.temp >= other.temp

	def __gt__(self, other):
		return self.temp > other.temp

	def __lt__(self, other):
		return self.temp < other.temp

	def __le__(self, other):
		return self.temp <= other.temp

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
	return (celsius * 9 / 5) + 32


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

print('All Temperature Readings:')
print(*readings, sep=", ")

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
print('Temperatures above 14.0:', *higher_temperatures)

# Find minimum, maximum etc in readings
print('Min temp in list =', minimum(readings))
print('Max temp in list =', maximum(readings))
print('Average temperature = {:.2f}'.format(average(readings)))
print('Median temperature value =', median(readings))
readings_range = data_range(readings)
print('Range of temperatures from ', str(readings_range[0].temp) + ' to ' + str(readings_range[1].temp))

# Add temperatures together
new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + TemperatureReading(15.5, '01/05/20', 'London', 'Celsius')
print('Add two temperatures', new_temperature)

new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5
print('Add a temperature and a int', new_temperature)

new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5.5
print('Add a temperature and a float', new_temperature)

print('Done')
