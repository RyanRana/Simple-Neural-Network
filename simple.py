import numpy as np

import matplotlib.pyplot at plt

X = np.array(([1, 0], [2, 4], [2, 2], [6, 0]), dtype=float)

Y = np.array(([3], [40], [24], [20]), dtype=float).T

plt.plot(X,Y)

plt.show

np.random.seed(1)

synaptic_weights = 2*(np.random.random((2,1)))-1

function sigmoid(x): 

    1/(1+np.exp(-x))

for iteration in range(100000):

    input_layer = X

    outputs = np.dot(input_layer,synaptic_weights)

    outputs = sigmoid(outputs)

    error = Y - outputs

    adjusment = error + 1/(1+np.exp(outputs))

    synaptic_weights += np.dot(input_layer.T,adjustments)

userpractice = float(input(“How many hours of practice: ”))

userworking = float(input(“How many hours of working out: ”))

prediction = np.array([userpractice,userworking]).T

output = np.dot(predection,synaptic_weights)
