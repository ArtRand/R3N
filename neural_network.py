#!/usr/bin/env python
"""
Citations
[1]http://cs231n.github.io/neural-networks-case-study/
[2]http://nbviewer.ipython.org/github/dennybritz/nn-from-scratch/blob/master/nn-from-scratch.ipynb
[3]https://github.com/mnielsen/neural-networks-and-deep-learning
"""

import numpy as np
from itertools import izip


class NeuralNetwork(object):
    """[3], [2]
    """
    def __init__(self, dimensions, activation_function):
        # eg. dimensions = [2, 10, 3] makes a 2-input, 10 hidden, 3 output NN
        self.layers = len(dimensions)
        np.random.seed(0)
        self.weights = [np.random.randn(x, y) / np.sqrt(x) for x, y, in zip(dimensions[:-1], dimensions[1:])]
        self.biases = [np.zeros((1, y)) for y in dimensions[1:]]
        self.activation = activation_function

    def predict(self, a):
        activation = a
        z = None
        # forward pass
        for bias, weight in izip(self.biases, self.weights):
            z = np.dot(activation, weight) + bias   # calculate input
            activation = self.activation(z, False)  # put though activation function
        # get softmax from final layer input
        exp_scores = np.exp(z)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

        return probs

    def fit(self, samples, labels, epochs=10000, epsilon=0.01, lbda=0.01, print_loss=False):
        for i in xrange(0, epochs):
            # first do the forward pass, keeping track of everything
            zs = []                       # list to store z vectors
            activation = samples          # initialize to input data
            activations = [samples, ]     # list to store activations

            for bias, weight in izip(self.biases, self.weights):
                z = np.dot(activation, weight) + bias   # calculate input
                zs.append(z)                            # keep track
                activation = self.activation(z, False)  # put though activation function
                activations.append(activation)          # keep track

            # get softmax from final layer input
            exp_scores = np.exp(zs[-1])
            probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

            # backward pass
            delta = self.cost_derivate(probs, labels)
            # place to store gradients
            grad_w = [np.zeros(w.shape) for w in self.weights]
            grad_b = [np.zeros(b.shape) for b in self.biases]

            # initialize
            grad_w[-1] = np.dot(activations[-2].T, delta)
            grad_b[-1] = np.sum(delta, axis=0, keepdims=True)

            # backprop through the network, starting at the last hidden layer
            for layer in xrange(2, self.layers):
                delta = np.dot(delta, self.weights[-layer + 1].T) * self.activation(activations[-layer], True)
                grad_w[-layer] = np.dot(activations[-layer - 1].T, delta)
                grad_b[-layer] = np.sum(delta, axis=0)

            # regularize the gradient on the weights
            grad_w = [gw + lbda * w for gw, w in izip(grad_w, self.weights)]

            # update based on learning rate (epsilon)
            self.weights = [w + -epsilon * dw for w, dw in izip(self.weights, grad_w)]
            self.biases = [b + -epsilon * db for b, db in izip(self.biases, grad_b)]

            if print_loss and i % 1000 == 0:
                loss = self.calculate_loss(samples, labels)
                accuracy = self.evaluate(samples, labels)
                print "Loss after iteration %i: %f accuracy: %0.2f" % (i, loss, accuracy)

        print "training accuracy: %0.2f" % self.evaluate(samples, labels)

    def cost_derivate(self, output_probs, labels):
        output_probs[range(len(labels)), labels] -= 1
        return output_probs

    def calculate_loss(self, input_data, labels, reg_lambda=0.01):
        num_examples = len(input_data)
        assert len(input_data) == len(labels)

        probs = self.predict(input_data)

        # Calculating the loss
        corect_logprobs = -np.log(probs[range(num_examples), labels])
        data_loss = np.sum(corect_logprobs)

        # Add regulatization term to loss (optional)
        for w in self.weights:
            data_loss += 0.5 * reg_lambda * np.sum(np.square(w))

        return float(1. / num_examples * data_loss)

    def evaluate(self, X, labels):
        probs = self.predict(X)
        hard_calls = np.argmax(probs, axis=1)
        return np.mean(hard_calls == labels)
