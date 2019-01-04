import warnings

import numpy as np
import matplotlib.pyplot as plt


from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

def my_derivation(x):
    return np.exp(x)/(1 + np.exp(x))

def book_derviation(x):
    return 1/(1 + np.exp(-x))


if __name__ == '__main__':
    X = load_iris().data
    y = load_iris().target

    X_std = StandardScaler().fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    print(len(X_train), len(X_test))
    print(len(y_train), len(y_test))
    print(y_train)

    # lr = LogisticRegression().fit(X, y)
    # print('Unstandardized Errors:', sum(lr.predict(X) != y))
    #
    # lr = LogisticRegression().fit(X_std, y)
    # print('Standardized Errors:', sum(lr.predict(X_std) != y))

