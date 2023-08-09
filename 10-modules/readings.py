from utils import celsius_to_fahrenheit
from utils import fahrenheit_to_celsius

CELSIUS = "Celsius"
FAHRENHEIT = "Fahrenheit"

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

    def __repr__(self):
        return f'value={self.value}, date={self.date}, location={self.location}'

    def __str__(self):
        return str(self.value) + ' on ' + str(self.date) + ' at ' + str(self.location)


class TemperatureReading(Reading):
    """ Specialised version of Reading to incorporates temperature info """

    def __init__(self, temp, date, location, scale):
        super().__init__(temp, date, location)
        self.scale = scale

    def convert(self):
        """ convert the temperature to a different scale """
        if self.scale == CELSIUS:
            return TemperatureReading(celsius_to_fahrenheit(self.value),
                                      self.date,
                                      self.location,
                                      FAHRENHEIT)
        else:
            return TemperatureReading(fahrenheit_to_celsius(self.value),
                                      self.date,
                                      self.location,
                                      CELSIUS)

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value + other
        else:
            new_value = self.value + other.value
        return TemperatureReading(new_value, self.date, self.location, self.scale)

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value - other
        else:
            new_value = self.value - other.value
        return TemperatureReading(new_value, self.date, self.location, self.scale)

    def __repr__(self):
        return f'TemperatureReading({super().__repr__()}, {self.scale})'

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
        else:
            new_value = self.value + other.temp
        return RainfallReading(new_value, self.date, self.time, self.location)

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value - other
        else:
            new_value = self.value - other.temp
        return RainfallReading(new_value, self.date, self.time, self.location)

    def __repr__(self):
        return f'RainfallReading {super().__repr__()}, time={self.time})'

    def __str__(self):
        return 'RainfallReading[' + self.time + '](' + super().__str__() + ')'

