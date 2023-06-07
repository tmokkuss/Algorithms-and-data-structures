import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

mnist = fetch_openml('mnist_784', version=1, cache=True)

X = mnist.data
y = mnist.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

n_estimators_list = [10, 50, 100, 200, 500]
best_accuracy = 0
best_n_estimators = None

for n_estimators in n_estimators_list:
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_n_estimators = n_estimators

print(f"Наилучшее количество деревьев: {best_n_estimators}")
print(f"Точность наилучшей модели: {best_accuracy}")

knn_model = KNeighborsClassifier()
svm_model = SVC()

knn_model.fit(X_train, y_train)
svm_model.fit(X_train, y_train)

knn_y_pred = knn_model.predict(X_test)
svm_y_pred = svm_model.predict(X_test)

knn_accuracy = accuracy_score(y_test, knn_y_pred)
svm_accuracy = accuracy_score(y_test, svm_y_pred)

print(f"Точность модели Random Forest: {best_accuracy}")
print(f"Точность модели k-NN: {knn_accuracy}")
print(f"Точность модели SVM: {svm_accuracy}")