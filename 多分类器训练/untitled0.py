# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:10:32 2020

@author: 卢玉德
"""

import numpy as np

LOCK=3
UNLOCK=0

generation=10000
learningrate=10000.0

def func(k,r):
    if k==r:
        return 1
    return 0

def reset():
    global r
    global yc
    global theta0
    global forecast0
    global subforecast0
    global derivative0
    global cost0
    global lock
    global learningrate
    global g

    theta0=[0]*(n+1)
    theta0=np.array(theta0)
    forecast0=(np.dot(theta0,X.transpose()))
    subforecast0=(forecast0-yc[r])
    derivative0=np.dot(subforecast0.transpose(),X)
    cost0=np.dot(subforecast0,subforecast0.transpose())
    g=0
    lock=[LOCK]
    learningrate*=0.7

def caltheta1():
    global r
    global yc
    global theta1
    global forecast1
    global subforecast1
    global cost1
    global derivative1
    
    theta1=theta0-learningrate*derivative0
    forecast1=np.dot(theta1,X.transpose())
    subforecast1=(forecast1-yc[r])
    derivative1=np.dot(subforecast1.transpose(),X)
    cost1=np.dot(subforecast1,subforecast1.transpose())

def thetachange():
    global theta0
    global forecast0
    global subforecast0
    global derivative0
    global cost0
    
    theta0=theta1
    forecast0=forecast1
    subforecast0=subforecast1
    derivative0=derivative1
    cost0=cost1

fpr=open('testcaseforreginal.txt','r')
fpr.readline()
m,n,c=tuple([int(i) for i in (fpr.readline()).split()])
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
yc=[]
for r in range(c):
    yc[r]=[func(k,r) for k in y]
    yc[r]=np.array(yc[r])
y=np.array(y)

fpw1=open('record.txt','w')
fpw2=open('result.txt','w')

fpw2.writelines("%d %d\n"%(n,c))

r=0
while r<c:
    fpw1.writelines("Now C is %d\n"%c)
    fpw1.writelines("Now learning rate:%.6lf\n"%learningrate);
    reset()
    while g<=generation:
        caltheta1()
        if cost0<cost1-1:
            lock[0]-=1
            fpw1.writelines("Error on generation %d\n"%(g+1))
            fpw1.writelines("cost[%d] is %.6f\n"%(g,cost0))
            fpw1.writelines("cost[%d] is %.6f\n"%(g+1,cost1))
        if lock[0]==UNLOCK or cost1>1e20:
            fpw1.writelines("----------------------------------")
            fpw1.writelines("Failed in generation %d\n"%(g+1))
            fpw1.writelines("Now learning rate:%.6lf\n"%learningrate);
            reset()
            continue
        thetachange()
        fpw1.writelines("generation %d:\n"%(g+1))
        fpw1.writelines("cost:%.6f\n"%cost1)
        fpw1.writelines(str(theta1)+"\n")
        g+=1
    fpw1.writelines("\n")
    for i in range(n+1):
        fpw2.writelines("%.6f "%theta1[i])
    fpw2.writelines("\n")
    r+=1
fpw1.writelines("terminated.\n")
fpw1.close()
fpw2.close()