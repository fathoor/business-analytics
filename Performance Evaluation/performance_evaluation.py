#!/usr/bin/python

from sklearn.metrics import classification_report

actual_email = [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1]
predicted_email = [0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0]

# Cari Confusion Matrix (TP, TN, FP, FN)
def confusion_matrix(actual, predicted):
    TP, TN, FP, FN = 0, 0, 0, 0

    for i in range(len(actual)):
        if actual[i] == 1 and predicted[i] == 1:
            TP += 1
        elif actual[i] == 0 and predicted[i] == 0:
            TN += 1
        elif actual[i] == 0 and predicted[i] == 1:
            FP += 1
        elif actual[i] == 1 and predicted[i] == 0:
            FN += 1
    
    return TP, TN, FP, FN

TP, TN, FP, FN = confusion_matrix(actual_email, predicted_email)

print("TP: {}\nTN: {}\nFP: {}\nFN: {}\n".format(TP, TN, FP, FN))

# Cari Accuracy
def accuracy(actual, predicted):
    TP, TN, FP, FN = confusion_matrix(actual, predicted)
    return (TP + TN) / (TP + TN + FP + FN)

print("Accuracy: {0:.3g}".format(accuracy(actual_email, predicted_email)))

# Cari Precision
def precision(actual, predicted):
    TP, TN, FP, FN = confusion_matrix(actual, predicted)
    return TP / (TP + FP)

print("Precision: {0:.3g}".format(precision(actual_email, predicted_email)))

# Cari Recall
def recall(actual, predicted):
    TP, TN, FP, FN = confusion_matrix(actual, predicted)
    return TP / (TP + FN)

print("Recall: {0:.3g}".format(recall(actual_email, predicted_email)))

# Cari F-Measure
def f_measure(actual, predicted):
    TP, TN, FP, FN = confusion_matrix(actual, predicted)
    return 2 * (precision(actual, predicted) * recall(actual, predicted)) / (precision(actual, predicted) + recall(actual, predicted))

print("F-Measure: {0:.3g}\n".format(f_measure(actual_email, predicted_email)))

# Accuracy, Precision, Recall, dan F-Measure menggunakan scikit-learn
print(classification_report(actual_email, predicted_email))