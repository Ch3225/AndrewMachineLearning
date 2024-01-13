# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:01:55 2020

@author: 卢玉德
"""

fpr=open('data.txt','r')
fpw=open('testcaseforreginal.txt','w')
fpw.writelines(fpr.readline())
m,n=tuple([int(i) for i in (fpr.readline()).split()])
fpw.writelines(""+str(m)+" 5\n")
for l in range(m):
    x,y,i=tuple([float(i) for i in (fpr.readline()).split()])
    fpw.writelines("%02.6f %02.6f %02.6f %02.6f %02.6f %.f\n"\
                   %((x*x),(y*y),(x*y),x,y,i))
fpw.close()
fpr.close()