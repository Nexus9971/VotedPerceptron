import numpy as np

def vector_sum(f, g):
    z = list()
    for i in range (0, len(f)):
        z.append(f[i]+g[i])
    return z

def scalar_product(f, g):
    z = 0
    for i in range (0, len(f)):
        z += (f[i]*g[i])
    return z

def scalar_vector(f, k):
    z = list()
    for i in range (0, len(f)):
        z.append(k*f[i])
    return z 