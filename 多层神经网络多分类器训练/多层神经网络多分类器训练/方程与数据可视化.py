# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:50:29 2020

@author: 卢玉德
"""

import numpy as np
import matplotlib.pyplot as plt

fpr1=open('TrainingExamples.txt','r')
fpr1.readline()
m,n,c=tuple([int(i) for i in (fpr1.readline()).split()])

for l in range(m):
    x,y,ans=tuple([float(i) for i in (fpr1.readline()).split()])
    if ans==2:
        plt.scatter(x,y,c="#ff12FF")
    elif ans==1:
        plt.scatter(x,y,c="#ff1212")
    else:
        plt.scatter(x,y,c="#00BFFF")

fpr1.close()
fpr2=open('result.txt','r')
n,t=tuple([int(i) for i in (fpr2.readline()).split()])
theta=[]
for r in range(t):
    theta.append([float(i) for i in (fpr2.readline()).split()])
fpr2.close()

x=[]
x.append(1)
for i in range(n):
    x.append(np.arange(-10,10,0.1))
x[1],x[2]=np.meshgrid(x[1],x[2])
z=[]
for i in range(t):
    z.append(0)
    for j in range(n+1):
        z[i]+=theta[i][j]*x[j]
    plt.contour(x[1],x[2],z[i],0)
plt.show()