CELSIUS = "Celsius"
FAHRENHEIT = "Fahrenheit"


class TemperatureReading:
    """ Class representing temperature info """

    def __init__(self, temp, date, location, scale=CELSIUS):
        self.temp = temp
        self.date = date
        self.location = location
        self.scale = scale

    def convert(self):
        """ convert the temperature to a different scale """
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

    def __str__(self):
        return f'TemperatureReading[{self.scale}]({self.temp} on {self.date} at {self.location})'


def average(data):
    if isinstance(data[0], int):
        return sum(data) / len(data)
    else:
        raw_data = list(map(lambda r: r.temp, data))
        return sum(raw_data) / len(raw_data)


def minimum(data, index=0):
    result = None
    if index == 0:
        data_slice = data
    else:
        data_slice = data[index:]
    for item in data_slice:
        if result is None:
            result = item
        elif result.temp > item.temp:
            result = item
    return result


def maximum(data, index=0):
    result = None
    if index == 0:
        data_slice = data
    else:
        data_slice = data[index:]
    for item in data_slice:
        if result is None:
            result = item
        elif result.temp < item.temp:
            result = item
    return result


def data_range(data):
    return minimum(data), maximum(data)


def extract_readings(reading):
    return reading.temp


def median(data):
    data.sort(key=extract_readings)
    print(*data, sep=", ")

    # sorted_data = bubble_sort(data)
    data_length = len(data)
    index = (data_length - 1) // 2

    if data_length % 2:
        return data[index]
    else:
        return (data[index] + data[index + 1]) / 2.0


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Set up the data the data file
readings = [
        TemperatureReading(13.5, '01/05/20', 'London', CELSIUS),
        TemperatureReading(12.6, '02/05/20', 'London', CELSIUS),
        TemperatureReading(15.3, '03/05/20', 'London', CELSIUS),
        TemperatureReading(12.2, '04/05/20', 'London', CELSIUS),
        TemperatureReading(16.6, '05/05/20', 'London', CELSIUS),
        TemperatureReading(14.6, '05/05/20', 'London', CELSIUS),
        TemperatureReading(15.6, '05/05/20', 'London', CELSIUS)
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

temp1 = TemperatureReading(13.5, '01/05/20', 'London', CELSIUS)
temp2 = temp1.convert()
print(f'temp1: {temp1}')
print(f'temp2: {temp2}')

print('Done')
