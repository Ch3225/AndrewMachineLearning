# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:34:32 2020

@author: 卢玉德
"""

import numpy as np
fpr=open('testcaseforreginal.txt','r')
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
Xt=np.transpose(X)
XtXinv=np.linalg.inv(np.dot(Xt,X))
theta=np.dot(np.dot(XtXinv,Xt),np.transpose(y))
fpw=open('testcaseforreginalresult.txt','w')
fpw.writelines(str(theta)+"\n")
fpw.close()