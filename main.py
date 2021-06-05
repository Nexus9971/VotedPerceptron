from Voted_Perceptron import Voted_Perceptron
import csv
from numpy.core.arrayprint import IntegerFormat
from numpy.lib.function_base import append
import random
from sklearn import metrics as skl

train_sample_percentage = 80
X = list()
Y = list()
with open('qsar_androgen_receptor.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    temp = list()
    for row in csv_reader:
        temp.clear()
        for i in range(0, len(row)-1):
            temp.append(int(row[i]))
        X.append(temp)
        Y.append(row[len(row)-1])
for i in range (0, len(Y)):
    if(Y[i] == "positive"):
        Y[i] = 1
    else:
        Y[i] = -1
for k in range (0, 10):
    indexes = list()
    stop = (len(Y)/100)*80
    stop = int(stop)
    random.seed(k)
    X_train = list()
    X_test = list()
    Y_train = list()
    Y_test = list()
    while len(indexes) < stop:
        temp = random.randint(0, stop-1)
        if temp not in indexes:
            indexes.append(temp)
    for i in range (0, len(Y)):
        if(i in indexes):
            X_train.append(X[i])
            Y_train.append(Y[i])
        else:
            X_test.append(X[i])
            Y_test.append(Y[i])
    classifier = Voted_Perceptron(5)
    pred = classifier.fit(X_train, Y_train)
    result = classifier.predict(X_test)
    print(skl.accuracy_score(Y_test, result))
#t = 0
#for i in range (0, len(result)):
#    if(result[i] != Y_test[i]):
#        t += 1
#print(t)