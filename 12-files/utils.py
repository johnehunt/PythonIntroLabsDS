def average(data):
	if isinstance(data[0], int):
		return sum(data) / len(data)
	else:
		raw_data = list(map(lambda r: r.value, data))
		return sum(raw_data) / len(raw_data)


def minimum(data):
	return min(data)


def maximum(data):
	return max(data)


def data_range(data):
	return minimum(data), maximum(data)


def median(data):
	sorted_data = sorted(data)
	data_length = len(data)
	index = (data_length - 1) // 2

	if data_length % 2:
		return sorted_data[index]
	else:
		return (sorted_data[index] + sorted_data[index + 1]) / 2.0
