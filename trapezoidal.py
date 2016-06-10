import matplotlib.pyplot as plt
import numpy as np
from math import *
import sys

# Calculates height
def height(high, lower, interval):
	return (high - lower) / interval

# Creates X axis
def xAxis(high, lower, height):
	return np.arange(lower, high, height)

# Creates y axis
def yAxis(xAxis, function):
	array = []
	for x in xAxis:
		array.append(eval(function))
	return array

# Calculates the total area
def area(yAxis, h):
	area = 0.0
	for index in range(1, len(yAxis)):
		area += ((yAxis[index - 1] + yAxis[index]) * h) / 2
	return area

# plot the graph
def plot(xAxis, yAxis, function, interval, h):
	plt.plot(xAxis, yAxis, 'ro', xAxis, yAxis, 'b')

	# Draw vertical and diagonal lines
	for index in range(1, len(xAxis)):
		plt.plot([xAxis[index - 1], xAxis[index]], [yAxis[index - 1], yAxis[index]], 'r--')
		plt.plot([xAxis[index], xAxis[index]], [0, yAxis[index]], 'r--')

	plt.title('Bisection Method\nf(x) = {}; intervalos = {}; area total = {}'.format(function, interval, area(yAxis, h)))
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True)
	plt.show()

def main(argv):
	if len(argv) == 3:
		interval = int(argv[0])
		range = np.fromstring(argv[1], dtype = float, sep = ',')
		lower = range[0]
		high = range[1]
		function = argv[2]

		h = height(high, lower, interval)
		x = xAxis(high,lower, h)
		y = yAxis(x, function)
		plot(x, y, function, interval, h)
	else:
		print("{} <iteration> <Xmin,Xmax> <function>".format(sys.argv[0]))
# Only run if a scritp
if __name__ == "__main__":
	main(sys.argv[1:])
