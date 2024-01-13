# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:50:29 2020

@author: 卢玉德
"""

import numpy as np
import matplotlib.pyplot as plt

fpr=open('linarydata.txt','r')
fpr.readline()
m,n=tuple([int(i) for i in (fpr.readline()).split()])

for l in range(m):
    x,y,ans=tuple([float(i) for i in (fpr.readline()).split()])
    if ans>0.5:
        plt.scatter(x,y,c="#ff1212")
    else:
        plt.scatter(x,y,c="#00BFFF")

x=np.arange(-7,7,0.1)
y=np.arange(-7,7,0.1)
x,y=np.meshgrid(x,y)
#z=np.power(x-1,2)+np.power(y,2)+1.5*(x-1)*y-4

z=x+2*y-3;
r=-6.47177873+2.19129089*x+4.48714408*y
plt.contour(x,y,z,0)
plt.contour(x,y,r,0)
plt.show()