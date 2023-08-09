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
        return f'RainfallReading({super().__repr__()}, time={self.time})'

    def __str__(self):
        return 'RainfallReading[' + self.time + '](' + super().__str__() + ')'


def average(data):
    if isinstance(data[0], int):
        return sum(data) / len(data)
    else:
        raw_data = list(map(lambda r: r.value, data))
        return sum(raw_data) / len(raw_data)


def minimum(data, index=0):
    if index == 0:
        data_slice = data
    else:
        data_slice = data[index:]
    return min(data_slice)


def maximum(data, index=0):
    if index == 0:
        data_slice = data
    else:
        data_slice = data[index:]
    return max(data_slice)


def data_range(data):
    return minimum(data), maximum(data)


def extract_readings(reading):
    return reading.temp


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


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Set up the data
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
print(readings)

# Convert all the temperatures from Celsius to fahrenheit
fahrenheit_temperatures = list(map(lambda r: celsius_to_fahrenheit(r.value), readings))
print('Fahrenheit Temperatures:', fahrenheit_temperatures)

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

# Add temperatures together
new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + TemperatureReading(15.5, '01/05/20',
                                                                                                 'London', 'Celsius')
print('Add two temperatures', new_temperature)

new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5
print('Add a temperature and a int', new_temperature)

new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5.5
print('Add a temperature and a float', new_temperature)

# Working with Rainfall readings
rainfall_readings = [
        RainfallReading(2.0, '01/05/20', '11:00', 'London'),
        RainfallReading(2.6, '02/05/20', '11:30', 'London'),
        RainfallReading(2.3, '03/05/20', '11:00', 'London'),
        RainfallReading(3.2, '04/05/20', '12:00', 'London'),
        RainfallReading(1.6, '05/05/20', '10:45', 'London')
]

print('All Rainfall Readings:')
print(rainfall_readings, sep=", ")
print(f'Average rainfall {average(rainfall_readings)}')

print('Done')
