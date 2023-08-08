# Illustrates use of higher order functions such as filter and map

def average(data):
    return sum(data) / len(data)


def median(data):
    sorted_data = sorted(data)
    data_length = len(data)
    index = (data_length - 1) // 2

    if data_length % 2:
        return sorted_data[index]
    else:
        return (sorted_data[index] +
                sorted_data[index + 1]) / 2.0


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


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Set up the data
readings = [13.5, 12.6, 15.3, 12.2, 16.6, 14.6, 15.6]

print(f'Readings: {readings}')

print('-' * 25)

# Convert all the temperatures from Celsius to Fahrenheit
fahrenheit_temperatures = list(map(celsius_to_fahrenheit, readings))
print(f'Fahrenheit Temperatures: {fahrenheit_temperatures}')

fahrenheit_temperatures2 = list(map(lambda celsius: (celsius * 9 / 5) + 32, readings))
print(f'Fahrenheit Temperatures2: {fahrenheit_temperatures2}')

# Find all temperatures above 14.0
higher_temperatures = list(filter(lambda t: t > 14.0, readings))
print(f'Temperatures above 14.0: {higher_temperatures}')

# Convert all readings above 14.0 to Fahrenheit
converted_temperatures = list(map(celsius_to_fahrenheit,
                                  filter(lambda t: t > 14.0, readings)))
print(f'Fahrenheit Temperatures above 14.0c: {converted_temperatures}')

print('- printing')

print(list(map(lambda t: f'{t:.2f}', converted_temperatures)))

# List comprehension
output = [f'{t:.2f}' for t in converted_temperatures]
print(output)

print('Done')
