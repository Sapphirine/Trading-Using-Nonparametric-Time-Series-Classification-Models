import math
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import cross_validation
my_data=genfromtxt('C:/Users/kimi/bitfinexUSD.csv',delimiter=',')
a=[]
b=[]
c=[]
for i in range(len(my_data)):
    a.append(my_data[i][0])
    b.append(my_data[i][1])
    c.append(my_data[i][2])
a1=[]
price=[]
c1=[]
for i in range(len(my_data)/60):
    x=0
    y=0
    z=0
    for j in range(60):
        x+=b[i*60+j]
        z+=c[i*60+j]
    y=a[i*60]
    x=x/60
    a1.append(y)
    price.append(x)
    c1.append(z)

minus=[]

for i in range(len(price)-1):
    t=price[i+1]-price[i]
    if t>0:
        t=1
    else:
        t=-1
    minus.append(t)

xx, yy = np.meshgrid(np.linspace(0, 4, 500),
                     np.linspace(0, 4, 500))
np.random.seed(0)

clf=svm.SVC(kernel='linear',C=1)
clf=svm.SVC(kernel='poly',degree=7,C=5)
clf=svm.SVC(kernel='rbf',gamma=10,C=2)
clf=svm.LinearSVC()
sss = cross_validation.StratifiedShuffleSplit(label, n_iter=3, test_size=0.4, random_state=0)
for train_index, test_index in sss:
    X_train, X_test = x[train_index], x[test_index]
    y_train, y_test = label[train_index], label[test_index] 
print clf.fit(X_train,y_train)
scores = cross_validation.cross_val_score(clf, X_test, y_test, cv=5, score_func=None)
print scores
#svc=svm.SVC(kernel='linear')
#print svc.fit(x,label)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()), aspect='auto',
           origin='lower', cmap=plt.cm.PuOr_r)
contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2,
                       linetypes='--')
plt.scatter(a,b, s=30, c=label, cmap=plt.cm.Paired)
plt.xticks(())
plt.yticks(())
plt.axis([0, 4, 0, 4])
plt.show()

    


'''f=open('C:/Users/kimi/bitfinexUSD.csv','r')
data=f.read()
data=data.split('\r')
for i in range(len(data)):
	data[i]=data[i].split(',')
a=[]
b=[]
c=[]
for i in range(len(data)):
	a.append(float(data[i][0]))
	b.append(float(data[i][1]))
	c.append(float(data[i][2]))
print b'''
