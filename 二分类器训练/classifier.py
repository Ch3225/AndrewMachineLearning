# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:12:08 2020

@author: 卢玉德
"""

import numpy as np

LOCK=3
UNLOCK=0

generation=1000
learningrate=10000.0

def reset():
    global theta0
    global yp
    global suby
    global derivative
    global cost0
    global lock
    global learningrate
    global g
    global yp
    
    theta0=[0]*(n+1)
    theta0=np.array(theta0)
    yp=1/(1+pow(np.e,-np.dot(theta0,X.transpose())))
    suby=yp-y
    cost0=np.sum(-y*np.log(yp)-(1-y)*np.log(1-yp))
    derivative=np.dot(suby,X)/m
    g=1
    lock=[LOCK]
    learningrate*=0.7

def caltheta1():
    global theta1
    global yp
    global suby
    global cost1
    global derivative
    global theta0
    
    theta1=theta0-learningrate*derivative
    yp=1/(1+pow(np.e,-np.dot(theta1,X.transpose())))
    suby=yp-y
    derivative=np.dot(suby,X)/m
    cost1=np.sum(-y*np.log(yp)-(1-y)*np.log(1-yp))
def thetachange():
    global theta0
    global cost0
    global cost1
    
    theta0=theta1
    cost0=cost1

fpr=open('linarydata.txt','r')
fpr.readline()
m,n=tuple([int(i) for i in (fpr.readline()).split()])
X=[]
y=[]
for i in range(m):
    chart=[float(i) for i in (fpr.readline()).split()]
    y.append(chart[n])
    del chart[n]
    TMP=[1]
    TMP.extend(chart)
    X.append(TMP)
fpr.close()

X=np.array(X)
y=np.array(y)

fpw=open('linarydataresult.txt','w')
fpw.writelines("Now learning rate:%.6lf\n"%learningrate);
reset()

while g<generation:
    caltheta1()
    if cost0<cost1-0.01:
        lock[0]-=1
        fpw.writelines("Error on generation %d\n"%(g+1))
        fpw.writelines("cost[%d] is %.6f\n"%(g,cost0))
        fpw.writelines("cost[%d] is %.6f\n"%(g+1,cost1))
    if lock[0]==UNLOCK or cost1>1e20 or np.isnan(cost1):
        fpw.writelines("----------------------------------")
        fpw.writelines("Failed in generation %d\n"%(g+1))
        fpw.writelines("Now learning rate:%.6lf\n"%learningrate);
        reset()
        continue
    thetachange()
    fpw.writelines("generation %d:\n"%(g+1))
    fpw.writelines("cost:%.6f\n"%cost1)
    fpw.writelines(str(theta1)+"\n")
    g+=1

fpw.writelines("terminated.\n")
fpw.close()