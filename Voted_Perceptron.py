import numpy as np
import utils as utl
import math

class Voted_Perceptron:
    
    def __init__(self, t):
        self.max_iter = t
        self.weights = 0
        self.bias = 0
        self.costs = 0

    def fit(self, x, y):
        w = list()
        b = list()
        c = list()
        w.append(np.zeros(len(x[0])))
        b.append(0)
        c.append(0)
        R = np.linalg.norm(x[0], 2)
        for i in range(1, len(x)):
            temp = np.linalg.norm(x[i], 2)
            if(temp > R):
                R = temp
        k = 0
        for epoch in range(1, self.max_iter+1):
            for i in range(1, len(x)):
                temp = utl.scalar_product(w[k], x[i])
                if(y[i]*(temp+b[k]) <= 0):
                    temp = utl.vector_sum(w[k], utl.scalar_vector(x[i], y[i]))
                    w.append(temp)
                    temp = b[k]+(y[i]*math.pow(R, 2))
                    b.append(temp)
                    k += 1
                    c.append(1)
                else:
                    c[k] += 1
        self.weights = w
        self.bias = b
        self.costs = c

    def predict(self, x):
        pred = list()
        for i in x:
            temp = 0
            for j in range(0, len(self.weights)):
                internal_sign = utl.sgn(utl.scalar_product(self.weights[j], i) + self.bias[j])
                temp += (self.costs[j]*internal_sign)
            pred.append(utl.sgn(temp))
        return pred