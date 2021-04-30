
class Reading:
	"""Root class for all types of readings"""

	def __init__(self, value, date, location):
		self.value = value
		self.date = date
		self.location = location

	def __eq__(self, other):
		return self.value == other.value

	def __ne__(self, other):
		return self.value != other.value

	def __ge__(self, other):
		return self.value >= other.value

	def __gt__(self, other):
		return self.value > other.value

	def __lt__(self, other):
		return self.value < other.value

	def __le__(self, other):
		return self.value <= other.value

	def __add__(self, other):
		new_value = self.value + other.value
		return Reading(new_value, self.date, self.location)

	def __sub__(self, other):
		new_value = self.value - other.value
		return Reading(new_value, self.date, self.location)

	def __str__(self):
		return str(self.value) + ' on ' + str(self.date) + ' at ' + str(self.location)


class TemperatureReading(Reading):
	""" Specialised version of Reading to incorporates temperature info """

	def __init__(self, temp, date, location, scale):
		super().__init__(temp, date, location)
		self.scale = scale

	def temp(self):
		return self.value

	def __add__(self, other):
		new_value = self.value + other.value
		return TemperatureReading(new_value, self.date, self.location, self.scale)

	def __sub__(self, other):
		new_value = self.value - other.value
		return TemperatureReading(new_value, self.date, self.location, self.scale)

	def __str__(self):
		return 'TemperatureReading[' + self.scale + '](' + super().__str__() + ')'


class RainfallReading(Reading):
	""" Subclass of Reading designed for timed rainfall readings """

	def __init__(self, amount, date, time, location):
		super().__init__(amount, date, location)
		self.time = time

	def __add__(self, other):
		new_value = self.value + other.value
		return RainfallReading(new_value, self.date, self.time, self.location)

	def __sub__(self, other):
		new_value = self.value - other.value
		return RainfallReading(new_value, self.date, self.time, self.location)

	def __str__(self):
		return 'RainfallReading[' + self.time + '](' + super().__str__() + ')'


def average(data):
	if isinstance(data[0], int):
		return sum(data) / len(data)
	else:
		raw_data = list(map(lambda r: r.temp(), data))
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
	temperatures = list(map(lambda r: r.temp(), readings))
	print('Temperatures:', temperatures)
	dates = list(map(lambda r: r.date, readings))
	print('Dates:', dates)

	# Find all temperatures above 14.0
	higher_temperatures = list(filter(lambda r: r.temp() > 14.0, readings))
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
