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
        return f"TemperatureReading(temp={self.temp}, date='{self.date}', location='{self.location}', scale='{self.scale}')"

    def __str__(self):
        return f'TemperatureReading[{self.scale}]({self.temp} on {self.date} at {self.location})'

readings = [
        TemperatureReading(13.5, '01/05/20', 'London'),
        TemperatureReading(12.6, '02/05/20', 'London'),
        TemperatureReading(15.3, '03/05/20', 'London', CELSIUS),
        TemperatureReading(12.2, '04/05/20', 'London', CELSIUS),
        TemperatureReading(16.6, '05/05/20', 'London', CELSIUS),
        TemperatureReading(14.6, '05/05/20', 'London', CELSIUS),
        TemperatureReading(15.6, '05/05/20', 'London', CELSIUS)
]

print('All Temperature Readings:')
print(readings)

print('-' * 25)

print('Individual temperature readings:')
for temp in readings:
    print(temp)

print('-' * 25)

print('Convert Temperature reading:')
temp1 = TemperatureReading(13.5, '01/05/20', 'London', CELSIUS)
temp2 = temp1.convert()
print(f'temp1: {temp1}')
print(f'temp2: {temp2}')
