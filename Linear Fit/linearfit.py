import numpy as np
import matplotlib.pyplot as plt

# matrix triangulating
def triangulating(matrix):
	lines = matrix.shape[0]
	columns = matrix.shape[1]

	# Turns the pivot into one
	if matrix[0,0] != 1:
		for line in range(1):
			head = matrix[line,0]
			for colum in range(columns):
				if line == 0:
					matrix[line, colum] = matrix[line, colum] / head
	
	# Turns matrix in upper triangular
	pivot = matrix[0,0]
	for line in range(1, lines):
		head = matrix[line,0]
		for colum in range(columns):
			matrix[line, colum] = (head * matrix[line - 1, colum]) - (matrix[line, colum] * pivot)

	# turns main diagonal into one
	for line in range(1, lines):
		pivot = matrix[line, line]
		for colum in range(columns):
			matrix[line, colum] = matrix[line, colum] / pivot

	return matrix

# Builds a linear system in the format
	# aEx 	+ 	bn 		= Ey
	# aEx^2 + 	bEx 	= Exy
# from two lists
def buildMatrix(x, y):
	sumX = 0.0
	sumY = 0.0
	sumX2 = 0.0
	sumXY = 0.0
	for index in range(len(x)):
		sumX += x[index]
		sumY += y[index]
		sumXY += x[index]*y[index]
		sumX2 += pow(x[index], 2)
	return np.matrix([[sumX, len(x), sumY], [sumX2, sumX, sumXY]])

# find the matrix coefficients
def coefficients(matrix):
	b = matrix[matrix.shape[0] - 1, matrix.shape[1] - 1]
	a = (matrix[matrix.shape[0] - 2, matrix.shape[1] - 1]) - (b * matrix[matrix.shape[0] - 2, matrix.shape[1] - 2])	
	return (a, b)

# creates the y axis linear adjustment
def yAxis(xAxix, coeff):
	array = []
	for index in range(len(xAxix)):
		array.append(coeff[0] * xAxix[index] + coeff[1])
	return array

# plot the graph
def plot(x, y, y2, coeff):
	plt.plot(x, y, 'ro', x, y2, 'b--')
	plt.title('Ajuste Linear\ny = {}x + {}'.format(coeff[0], coeff[1]))
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True)
	plt.show()

# Only run as scritp
if __name__ == "__main__":
	
	x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	y = [2.9, 4.8, 7.2, 9, 11.3, 12.5, 15.1, 16.9, 19, 20.3]

	matrix = buildMatrix(x, y)
	matrix = triangulating(matrix)
	coeff = coefficients(matrix)
	yAxis = yAxis(xAxix = x, coeff = coeff)
	plot(x, y, yAxis, coeff)

