from math import isclose

from readings import TemperatureReading
from readings import CELSIUS
from utils import *

data = [2, 3, 4, 5, 6, 5, 4]

readings = [
		TemperatureReading(14.5, '01/01/21', 'London', CELSIUS),
		TemperatureReading(15.5, '02/01/21', 'London', CELSIUS),
		TemperatureReading(16.5, '03/01/21', 'London', CELSIUS)
]


def test_min_int():
	result = minimum(data)
	assert result == 2


def test_min_temperature():
	result = minimum(readings)
	assert result == TemperatureReading(14.5, '01/01/21', 'London', CELSIUS)


def test_max_int():
	result = maximum(data)
	assert result == 6


def test_max_temperature():
	result = maximum(readings)
	assert result == TemperatureReading(16.5, '03/01/21', 'London', CELSIUS)


def test_average_int():
	result = average(data)
	assert isclose(result, 4.1, rel_tol=0.05)


def test_average_temperature():
	result = average(readings)
	assert isclose(result, 15.5, rel_tol=0.05)


def test_median_int():
	result = median(data)
	assert result == 4


def test_median_temperature():
	result = median(readings)
	assert result == TemperatureReading(15.5, '02/01/21', 'London', CELSIUS)


def test_data_range_ints():
	result = data_range(data)
	assert result == (2, 6)


def test_data_range_temperatures():
	readings_range = data_range(readings)
	assert readings_range[0] == TemperatureReading(14.5, '01/01/21', 'London', CELSIUS)
	assert readings_range[1] == TemperatureReading(16.5, '03/01/21', 'London', CELSIUS)
