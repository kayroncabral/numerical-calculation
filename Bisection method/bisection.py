import matplotlib.pyplot as plt
import numpy as np

# Creates X axis
def xAxis():
	return np.arange(-1, 2, 0.01)

# Creates y axis
def yAxis(xAxis):
	array = []
	for value in xAxis:
		array.append(np.cos(np.pi*value))
	return array

# Returns de midpoint
def bisection(a, b, iterations):
	count = 0
	while count < iterations:
		xm = (a + b) / 2
		if y[a] * y[xm] < 0:
			b = xm
		else:
			a = xm
		count += 1
	return xm

# plot the graph
def plot(x, y, xm):
	plt.plot(x, y, 'r--', x[xm], 0, 'ro')
	plt.title('Bisection Method\ncos(x)')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True)
	plt.show()

# Only run if a scritp
if __name__ == "__main__":

	iterations = 100
	x = xAxis()
	y = yAxis(x)

	a = 0
	b = len(x) - 1

	xm = bisection(a, b, iterations)

	plot(x, y, xm)