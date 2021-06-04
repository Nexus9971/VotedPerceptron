import numpy as np
import math

class Voted_Perceptron_Fit:
    
    def __init__(self, t):
        self.max_iter = t

    def fit(self, x, y):
        w = list()
        b = list()
        c = list()
        w.append(np.zeros(len(x[0])))
        b.append(np.zeros(len(x[0])))
        c.append(0)
        R = np.linalg.norm(x[0], 2)
        for i in x:
            temp = np.linalg.norm(x[i], 2)
            if(temp > R):
                R = temp
        k = 0
        for epoch in range(1, self.max_iter+1):
            for i in range(1, len(x)):
                temp = np.dot(w[k], x[i])
                if(np.dot(y[i], np.sum(temp, b[k], axis=0)) <= 0):
                    temp = np.sum(w[k], np.dot(y[i], x[i]), axis=0)
                    w.append(temp)
                    temp = np.sum(b[k], np.array(y[i])*math.pow(R, 2), axis=0)
                    b.append(temp)
                    k += 1
                    c.append(1)
                else:
                    c[k] += 1
        self.weights = w
        self.bias = b
        self.costs = c
        return (w, b, c)

    def predict(self, x):
        temp = 0
        for i in range(1, len(self.weights)):
            internal_sgn = np.sum(self.b[i], np.dot(self.w[i], x), axis = 0)
            temp += self.costs[i]*internal_sgn
        return np.sign(temp)