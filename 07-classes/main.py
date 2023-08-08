CELSIUS = "Celsius"
FAHRENHEIT = "Fahrenheit"


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


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
                                      self.location)

    def __repr__(self):
        return f'TemperatureReading(temp={self.temp}, date={self.date}, location={self.location}, scale={self.scale})'

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



# Set up the data
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
print(readings)
print(len(readings))

# Find all temperatures above 14.0
higher_temperatures = list(filter(lambda t: t.temp > 14.0, readings))
print('Temperatures above 14.0:\n\t', higher_temperatures)

temp1 = TemperatureReading(13.5, '01/05/20', 'London', CELSIUS)
temp2 = temp1.convert()
print(f'temp1: {temp1}')
print(f'temp2: {temp2}')

print('Done')
