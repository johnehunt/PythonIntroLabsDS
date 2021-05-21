from utils import celsius_to_fahrenheit
from utils import fahrenheit_to_celsius

CELSIUS = "Celsius"
FAHRENHEIT = "Fahrenheit"


class InvalidTemperatureException(Exception):
	""" Valid Ages must be between 0 and 120 """

	def __init__(self, value, message):
		self.value = value
		self.message = message

	def __str__(self):
		return f'InvalidTemperatureException({self.value}, {self.message})'


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

	def convert(self):
		""" convert the temperature to a different scale """
		print(self.scale)
		print(CELSIUS)
		print(self.scale == CELSIUS)
		if self.scale == CELSIUS:
			return TemperatureReading(celsius_to_fahrenheit(self.temp),
			                          self.date,
			                          self.location,
			                          FAHRENHEIT)
		else:
			return TemperatureReading(fahrenheit_to_celsius(self.temp),
			                          self.date,
			                          self.location,
			                          CELSIUS)

	def __add__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			new_value = self.value + other
		elif isinstance(other, TemperatureReading):
			new_value = self.value + other.value
		else:
			# Something is wrong its not an int, a float or a temperature reading
			raise InvalidTemperatureException(other, 'Invalid type for addition to TemperatureReading')

		return TemperatureReading(new_value, self.date, self.location, self.scale)

	def __sub__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			new_value = self.value - other
		elif isinstance(other, TemperatureReading):
			new_value = self.value - other.value
		else:
			raise InvalidTemperatureException(other, 'Invalid type for subtraction from TemperatureReading')
		return TemperatureReading(new_value, self.date, self.location, self.scale)

	def __str__(self):
		return 'TemperatureReading[' + self.scale + '](' + super().__str__() + ')'


class RainfallReading(Reading):
	""" Subclass of Reading designed for timed rainfall readings """

	def __init__(self, amount, date, time, location):
		super().__init__(amount, date, location)
		self.time = time

	def __add__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			new_value = self.value + other
		elif isinstance(other, RainfallReading):
			new_value = self.value + other.value
		else:
			raise InvalidTemperatureException(other, 'Invalid type for addition to RainfallReading')
		return RainfallReading(new_value, self.date, self.time, self.location)

	def __sub__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			new_value = self.value - other
		elif isinstance(other, RainfallReading):
			new_value = self.value - other.value
		else:
			raise InvalidTemperatureException(other, 'Invalid type for subtraction from RainfallReading')
		return RainfallReading(new_value, self.date, self.time, self.location)

	def __str__(self):
		return 'RainfallReading[' + self.time + '](' + super().__str__() + ')'
