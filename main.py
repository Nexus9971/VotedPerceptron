from utils import get_stats, print_stats, load_data
from Voted_Perceptron import Voted_Perceptron
from sklearn import metrics as metr
import random


train_sample_percentage = int(input("Insert percentage of train: "))
train_sample_percentage /= 100
repetitions = int(input("Insert number of repetitions of training and prediction: "))
max_epochs = int(input("Insert number of max epochs for Perceptrons: "))
X = list()
Y = list()
acc = list()
f1 = list()
prec = list()
re = list()
choice = input("Choose which dataset to load (1, 2, or 3): ")
csv_reader = 0
print()

if choice == '1':
    X, Y = load_data('qsar_androgen_receptor.csv')
elif choice == '2':
    X, Y = load_data('qsar_oral_toxicity.csv')
elif choice == '3':
    X, Y = load_data('biodeg.csv')

for k in range(0, repetitions):
    indexes = list()
    stop = len(Y) * train_sample_percentage
    stop = int(stop)
    X_train = list()
    X_test = list()
    Y_train = list()
    Y_test = list()
    while len(indexes) < stop:
        temp = random.randint(0, len(X) - 1)
        if temp not in indexes:
            indexes.append(temp)
    for i in range(0, len(Y)):
        if (i in indexes):
            X_train.append(X[indexes.index(i)])
            Y_train.append(Y[indexes.index(i)])
        else:
            X_test.append(X[i])
            Y_test.append(Y[i])
    classifier = Voted_Perceptron(max_epochs)
    classifier.fit(X_train, Y_train)
    pred = classifier.predict(X_test)
    matri = metr.confusion_matrix(Y_test, pred)
    print("Confusion Matrix " + str(k + 1) + "-th iterations:")
    print(matri)
    acc.append(metr.accuracy_score(Y_test, pred))
    f1.append(metr.f1_score(Y_test, pred, zero_division=0))
    prec.append(metr.precision_score(Y_test, pred, zero_division=0))
    re.append(metr.recall_score(Y_test, pred, zero_division=0))
print("\n")
stats_matr = list()
stats_matr.append(get_stats(acc))
stats_matr.append(get_stats(f1))
stats_matr.append(get_stats(prec))
stats_matr.append(get_stats(re))
stats_label = list()
order = " [Mean, Variance, Standard Deviation]"
stats_label.append("Accuracy" + order)
stats_label.append("F1" + order)
stats_label.append("Precision" + order)
stats_label.append("Recall" + order)
print_stats(stats_label, stats_matr)