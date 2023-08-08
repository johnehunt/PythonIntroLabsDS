CELSIUS = "Celsius"
FAHRENHEIT = "Fahrenheit"


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
        if isinstance(other, int) or isinstance(other, float):
            return self.temp >= other
        else:
            return self.temp >= other.temp

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.temp > other
        else:
            return self.temp > other.temp

    def __lt__(self, other):
        return self.temp < other.temp

    def __le__(self, other):
        return self.temp <= other.temp

    def __repr__(self):
        return f'TemperatureReading({self.temp}, {self.date}, {self.location}, {self.scale})'

    def __str__(self):
        return 'TemperatureReading[' + self.scale + '](' + str(self.temp) + ' on ' + str(self.date) + ' at ' + str(
                self.location) + ')'


def average(data):
    if isinstance(data[0], int):
        return sum(data) / len(data)
    else:
        raw_data = list(map(lambda r: r.temp, data))
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
    return min(data), max(data)


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
print(readings)

# Find all temperatures above 14.0
higher_temperatures = list(filter(lambda t: t > 14.0, readings))
print('Temperatures above 14.0:', *higher_temperatures)

# Find minimum, maximum etc in readings
print('Min temp in list =', minimum(readings))
print('Max temp in list =', maximum(readings))
print('Average temperature = {:.2f}'.format(average(readings)))
print('Median temperature value =', median(readings))
readings_range = data_range(readings)
print('Range of temperatures from ', str(readings_range[0].temp) + ' to ' + str(readings_range[1].temp))

# Add temperatures together
new_temperature = (TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') +
                   TemperatureReading(15.5, '01/05/20', 'London', 'Celsius'))
print('Add two temperatures', new_temperature)

# Add an int to a temperature
new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5
print('Add a temperature and a int', new_temperature)

# Add a float to a temperature
new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5.5
print('Add a temperature and a float', new_temperature)

another_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius')
print(new_temperature > another_temperature)
print(new_temperature >= another_temperature)
print(new_temperature == another_temperature)
print(new_temperature != another_temperature)
print(new_temperature < another_temperature)
print(new_temperature <= another_temperature)

sorted_data = sorted(readings)
print(sorted_data)

print('Done')
