import numpy as np
import pandas as pd

#Initializing Parameters: Temporary: The matrix would ideally be extracted from the CSV file Swetha provides
#matrix is n x 10, n = 11
param = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
for i in range(10):
	param += [list(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) * np.random.randint(2, 10))]
#print(params)	#Debug 1: Params Created

#Assigns random weights in a 10 x 3 (parameters x results) matrix
weights = np.random.rand(10, 3)
params = np.array(param)
#print(weights)	#Debug 2: Weights assigned

#Initializing weights: Also supposed to come from csv, n x 3, n = 11
predT = [[1, 2, 3]]
for i in range(10):
	predT += [list(np.array([1, 2, 3,]) * i)]
# print(predT) #Debug 3: Prediction target matrix extracted

#Iterative Corrections
for i in range(1):#range(len(predT)):
	output = np.dot(params[i], weights)
	error = (output - predT[i]) ** 2
	delta = predT[i] - output
	print(delta)
	#print(delta) #Debug 4: delta is a 1x3 vector with absolute errors
	for j in range(len(weights[0])):
		wDel = params[i] * delta[j]
		print(wDel)
		weights[:, j] += wDel
		print(weights)








# b = np.matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20], [21, 22, 23], [24, 25, 26], [27, 28, 29]])
# c = np.dot(a, b)
# print(a)
# print(b)
# print(c)