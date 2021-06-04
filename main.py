import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.linear_model import Perceptron


X_train = fetch_20newsgroups(subset="train")
newsgroup_test = fetch_20newsgroups(subset="test")
Y_train = X_train.target
print(X_train.data[0])