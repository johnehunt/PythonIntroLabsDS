from math import isclose

import pytest
from assertpy import assert_that

from readings import TemperatureReading, CELSIUS
from utils import average, minimum, maximum, median, celsius_to_fahrenheit, fahrenheit_to_celsius, data_range


@pytest.fixture()
def temperatures():
    return [
            TemperatureReading(13.5, '01/05/20', 'London', CELSIUS),
            TemperatureReading(12.6, '02/05/20', 'London', CELSIUS),
            TemperatureReading(15.3, '03/05/20', 'London', CELSIUS),
            TemperatureReading(12.2, '04/05/20', 'London', CELSIUS),
            TemperatureReading(16.6, '05/05/20', 'London', CELSIUS),
            TemperatureReading(14.6, '05/05/20', 'London', CELSIUS),
            TemperatureReading(15.6, '05/05/20', 'London', CELSIUS)
    ]


@pytest.fixture()
def data():
    return [2, 3, 4, 5, 6, 5, 4]


def test_average(temperatures):
    result = average(temperatures)
    assert isclose(result, 14.34, rel_tol=0.01)


def test_median(temperatures):
    result_temp = median(temperatures)
    assert isclose(result_temp.value, 14.6, rel_tol=0.01)


def test_min_int(data):
    assert_that(minimum(data)).is_equal_to(2)


def test_max_int(data):
    result = maximum(data)
    assert result == 6


def test_celsius_to_fahrenheit():
    result = celsius_to_fahrenheit(12.3)
    assert isclose(result, 54.14, rel_tol=0.01)


def test_fahrenheit_to_celsius():
    result = fahrenheit_to_celsius(54.14)
    assert isclose(result, 12.3, rel_tol=0.01)

def test_data_range_ints(data):
	result = data_range(data)
	assert result == (2, 6)


def test_data_range_temperatures(temperatures):
    readings_range = data_range(temperatures)
    assert readings_range[0] == TemperatureReading(12.2, '04/05/20', 'London', CELSIUS)
    assert readings_range[1] == TemperatureReading(16.6, '05/05/20', 'London', CELSIUS)
