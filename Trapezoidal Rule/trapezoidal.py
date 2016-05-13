import matplotlib.pyplot as plt

# Calculates height
def height(high, lower, interval):
	return (high - lower) / interval

# Creates X axis
def xAxis(lower, high):
	array = []
	value = lower
	while value <= high:
		array.append(value)
		value += h
	return array

# Creates y axis
def yAxis(xAxis):
	array = []
	for index in range(len(xAxis)):
		array.append(pow(xAxis[index], 2))
	return array

# Calculates the total area
def area(yAxis, h):
	area = 0.0
	for index in range(1, len(yAxis)):
		area += ((yAxis[index - 1] + yAxis[index]) * h) / 2
	return area

# plot the graph
def plot(xAxis, yAxis, interval, h):
	plt.plot(xAxis, yAxis, 'ro', xAxis, yAxis, 'b')

	# Draw vertical and diagonal lines
	for index in range(1, len(xAxis)):
		plt.plot([xAxis[index - 1], xAxis[index]], [yAxis[index - 1], yAxis[index]], 'r--')
		plt.plot([xAxis[index], xAxis[index]], [0, yAxis[index]], 'r--')

	plt.title('Regra do Trapezio\nIntervalos: {} e Area total: {}'.format(interval, area(yAxis, h)))
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True)
	plt.show()

# Only run if a scritp
if __name__ == "__main__":

	lower = 0.0
	high = 3.0
	interval = 10

	h = height(high, lower, interval)
	x = xAxis(lower, high)
	y = yAxis(x)
	plot(x, y, interval, h)