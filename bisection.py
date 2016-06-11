import matplotlib.pyplot as plt
import numpy as np
from math import *
import sys

# Creates X axis
def xAxis(high, lower, h):
	return np.arange(lower, high, h)

# Creates y axis
def yAxis(xAxis, function):
	array = []
	for x in xAxis:
		array.append(eval(function))
	return array

# Returns de midpoint
def bisection(y, a, b, iterations):
	count = 0
	xm = (a + b) / 2
	while count < iterations:
		xm = (a + b) / 2
		if y[a] * y[xm] < 0:
			b = xm
		else:
			a = xm
		count += 1
	return xm

# plot the graph
def plot(x, y, xm, function):
	plt.plot(x, y, 'r--', x[xm], y[xm], 'ro')
	plt.title('Bisection Method\nf(x) = {}; xm = {}'. format(function, y[xm]))
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True)
	plt.show()

def main(argv):
	if len(argv) == 3:
		iterations = int(argv[0])
		range = np.fromstring(argv[1], dtype = float, sep = ',')
		x = xAxis(range[1], range[0], range[2])
		function = argv[2]
		y = yAxis(x, function)

		a = 0
		b = len(x) - 1

		xm = bisection(y, a, b, iterations)
		plot(x, y, xm, function)
	else:
		print("{} <iteration> <Xmin,Xmax,h> <function>".format(sys.argv[0]))

# Only run if a scritp
if __name__ == "__main__":
	main(sys.argv[1:])
