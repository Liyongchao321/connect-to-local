
from sklearn import datasets
from sklearn import svm
import matplotlib.pyplot as plt
iris= datasets.load_iris()
digits = datasets.load_digits()
X_iris= iris.data
y_iris= iris.target

# plt.imshow(digits.images[-1], cmap=plt.cm.gray_r) 


print(X_iris)
# clf = svm.SVC(gamma=0.001, C=100.)
# clf.fit(digits.data[:-1], digits.target[:-1])
# print(clf.predict(digits.data[-1:]))