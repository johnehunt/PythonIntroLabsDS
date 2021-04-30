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
