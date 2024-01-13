# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:10:32 2020

@author: 卢玉德
"""

import numpy as np

LOCK=3
UNLOCK=0

generation=40000
lamda=0.0001

def func(k,r):
    if k==r:
        return 1
    else:
        return 0

#惩罚值
def punish(y0,x0):
    return y0*np.log(x0+(1-x0)*promise)+(1-y0)*np.log(1-x0+(x0)*promise)

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
    thetaforlamda=np.array(theta0)
    thetaforlamda[0]=0
    yp=1/(1+pow(np.e,-np.dot(theta0,X.transpose())))
    suby=yp-yc[r]
    cost0=np.sum(-yc[r]*np.log(yp)-(1-yc[r])*np.log(1-yp))+lamda*np.sum(np.dot(thetaforlamda,thetaforlamda))/2/m
    derivative=np.dot(suby,X)/m+lamda*thetaforlamda/m
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
    thetaforlamda=np.array(theta1)
    thetaforlamda[0]=0
    yp=1/(1+pow(np.e,-np.dot(theta1,X.transpose())))
    suby=yp-yc[r]
    derivative=np.dot(suby,X)/m+lamda*thetaforlamda/m
    cost1=np.sum(-yc[r]*np.log(yp)-(1-yc[r])*np.log(1-yp))+lamda*np.sum(np.dot(thetaforlamda,thetaforlamda))/2/m
def thetachange():
    global theta0
    global cost0
    global cost1
    
    theta0=theta1
    cost0=cost1

fpr=open('TrainingExamples.txt','r')
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
    yc.append([func(k,r) for k in y])
    yc[r]=np.array(yc[r])
y=np.array(y)

fpw1=open('record.txt','w')
fpw2=open('result.txt','w')

fpw2.writelines("%d %d\n"%(n,c))

r=0
while r<c:
    fpw1.writelines("Now C is %d\n"%c)
    learningrate=10000.0
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