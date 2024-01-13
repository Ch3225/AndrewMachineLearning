# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 15:38:09 2020

@author: 卢玉德
"""

import numpy as np

fpr1=open("result.txt",'r')
n,t=tuple([int(i) for i in (fpr1.readline()).split()])
theta=[]
for r in range(t):
    theta.append([float(i) for i in (fpr1.readline()).split()])
fpr1.close()
theta=np.array(theta)
fpr2=open("TestingExamples.txt",'r')
fpr2.readline()
m,n,c=tuple([int(i) for i in (fpr2.readline()).split()])

X=[]
y=[]
for i in range(m):
    chart=[float(i) for i in (fpr2.readline()).split()]
    y.append(chart[n])
    del chart[n]
    TMP=[1]
    TMP.extend(chart)
    X.append(TMP)
fpr2.close()

X=np.array(X)
y=np.array(y)

yp=1/(1+pow(np.e,-(np.dot(theta,X.transpose())).transpose()))
print(yp)
