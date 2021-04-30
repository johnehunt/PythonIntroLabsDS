# Defines functions associated with loading the csv file
import csv

from readings import TemperatureReading


def load_data(filename):
	data = []
	print('Loading file', filename)
	with open(filename, newline='') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			row_length = len(row)
			if row_length != 4:
				print('Error in data (length is not 3):', row)
				print('In line:', reader.line_num)
			else:
				temp = float(row[0])
				scale = row[1]
				date = row[2]
				location = row[3]
				reading = TemperatureReading(temp, date, location, scale)
				data.append(reading)
	print('Finished reading file')
	return data
