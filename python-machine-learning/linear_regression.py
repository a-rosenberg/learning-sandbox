import random


import numpy as np
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt


plt.style.use('ggplot')

x = np.array(list(range(10))).reshape(-1, 1)
y = [y + random.normalvariate(0, 1) for y in x * 1.7 + 3]



model = LinearRegression().fit(X=x, y=y)

plt.plot(x, y, '.')
plt.plot(x, model.predict(x), '-b')
print(model.coef_)
print(model.intercept_)
plt.show()
