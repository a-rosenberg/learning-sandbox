#!/usr/bin/env python

import numpy as np
import pandas as pd

class Perceptron(object):
    def __init__(self, eta=0.01, iterations=10, random_state=1):
        self.eta = eta
        self.iterations = iterations
        self.random_state = random_state

        self.w_ = None
        self.errors_ = None

    def fit(self, X, y):
        random_generator = np.random.RandomState(self.random_state)
        self.w_ = random_generator.normal(loc=0.0, scale=0.1, size=1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.iterations):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[0] += update  # intercept
                self.w_[1:] += update * xi
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def predict(self, X):
        net_input = np.dot(X, self.w_[1:]) + self.w_[0]
        return np.where(net_input >= 0.0, 1, -1)


if __name__ == '__main__':
    data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
    samples = 100
    X = data.iloc[0:samples, [0, 2]].values
    y = np.where(data.iloc[0:samples, -1:].values == 'Iris-setosa', -1, 1)

    perceptron = Perceptron()
    perceptron.fit(X, y)
    preds = perceptron.predict(X)
    for _ in zip(preds, data.iloc[0:samples, -1:].values):
        print(_)




