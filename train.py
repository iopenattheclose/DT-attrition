import pickle
import os
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier


with open('data/preprocessed_X_sm.pickle', 'rb') as handle:
    X_train = pickle.load(handle)

with open('data/X_test.pickle', 'rb') as handle:
    X_test = pickle.load(handle)

with open('data/y_sm.pickle', 'rb') as handle:
    y_train = pickle.load(handle)

with open('data/y_test.pickle', 'rb') as handle:
    y_test = pickle.load(handle)


