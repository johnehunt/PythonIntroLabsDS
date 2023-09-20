CELSIUS = "Celsius"
FAHRENHEIT = "Fahrenheit"

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

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
        return f"TemperatureReading(temp={self.temp}, date='{self.date}', location='{self.location}', scale='{self.scale}')"

    def __str__(self):
        return 'TemperatureReading[' + self.scale + '](' + str(self.temp) + ' on ' + str(self.date) + ' at ' + str(
                self.location) + ')'


# Add temperatures together
new_temperature = (TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') +
                   TemperatureReading(15.5, '01/05/20', 'London', 'Celsius'))
print('Add two temperatures:', new_temperature)

# Add an int to a temperature
new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5
print('Add a temperature and a int:', new_temperature)

# Add a float to a temperature
new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5.5
print('Add a temperature and a float:', new_temperature)

another_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius')
print(new_temperature > another_temperature)
print(new_temperature >= another_temperature)
print(new_temperature == another_temperature)
print(new_temperature != another_temperature)
print(new_temperature < another_temperature)
print(new_temperature <= another_temperature)


# readings = [
#         TemperatureReading(13.5, '01/05/20', 'London', 'Celsius'),
#         TemperatureReading(12.6, '02/05/20', 'London', 'Celsius'),
#         TemperatureReading(15.3, '03/05/20', 'London', 'Celsius'),
#         TemperatureReading(12.2, '04/05/20', 'London', 'Celsius'),
#         TemperatureReading(16.6, '05/05/20', 'London', 'Celsius'),
#         TemperatureReading(14.6, '05/05/20', 'London', 'Celsius'),
#         TemperatureReading(15.6, '05/05/20', 'London', 'Celsius')
# ]
# sorted_data = sorted(readings)
# print(sorted_data)
