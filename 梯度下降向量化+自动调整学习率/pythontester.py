# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:36:40 2020

@author: 卢玉德
"""

import numpy as np

theta1=np.array([1,1,1,1,1,1])
X=np.array([[1,1,1,1,1,1],[2,2,2,2,2,2]])
yp=1/(1+pow(np.e,np.dot(theta1,X.transpose())))
print(yp)