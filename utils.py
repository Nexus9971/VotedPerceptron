import math
import csv

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

def stat_mean(v):
    m = 0
    for i in v:
        m+=i
    m/=len(v) 
    return m

def stat_variance(v, mean):
    var = 0
    for i in v:
        var+= math.pow((i-mean), 2)
    if len(v) > 1:
        var/=(len(v)-1)
    else:
        var = 0
    return var

def get_stats(v):
    m = stat_mean(v)
    v = stat_variance(v, m)
    s = math.sqrt(v)
    return [m, v, s]

def print_stats(stats_label, stats_matr):
    for i in range(0, len(stats_matr)):
        print(stats_label[i])
        for j in range(0, len(stats_matr[0])):
            print(str(stats_matr[i][j]) + "\t", end='')
        print("\n")

def sgn(x):
    if(x > 0):
        return 1
    else:
        return -1

def load_data(s):
    X = list()
    Y = list()
    with open(s) as csv_file:
        f = csv.reader(csv_file, delimiter=';')

        if s == 'biodeg.csv':
            for row in f:
                X.append(row[0:len(row) - 1])
                Y.append(row[len(row) - 1])
            for i in range(0, len(X)):
                for j in range(0, len(X[i])):
                    X[i][j] = float(X[i][j])
            for i in range(0, len(Y)):
                if (Y[i] == "RB"):
                    Y[i] = 1
                else:
                    Y[i] = -1
        else:
            for row in f:
                X.append(row[0:len(row) - 1])
                Y.append(row[len(row) - 1])
            for i in range(0, len(X)):
                for j in range(0, len(X[i])):
                    X[i][j] = int(X[i][j])
            for i in range(0, len(Y)):
                if (Y[i] == "positive"):
                    Y[i] = 1
                else:
                    Y[i] = -1
    return X, Y