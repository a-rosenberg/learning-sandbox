import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.1, 'class2'],
    ['blue', 'XL', 15.4, 'class2'],
    ['red', 'M', 13.5, 'class1'],
])

df.columns = ['color', 'size', 'cost', 'class']

df['class'] = LabelEncoder().fit_transform(y=df['class'])
df = pd.get_dummies(df, drop_first=False)
df.info()

