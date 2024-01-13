# -*- coding: utf-8 -*-
"""
@author: 卢玉德
"""

#       *是矩阵按元素乘，相当于matlab里的点乘

import numpy as np

LOCK=7
UNLOCK=0

generation=300
lamda=0.01
downrate=0.7
learningrate=100.0
lock=10

#修正了公式中的log部分，避免爆INF
promise=0.00005

#归一化
"""
def gyh(pramaters):
    sum=0;
    bias=min(pramaters)
    pramaters=[i-bias for i in pramaters]
    for i in pramaters:
        sum+=i
    pramaters=[i/sum for i in pramaters]
    return pramaters
"""
def logisic(pramaters):
    return 1/(1+pow(np.e,pramaters)/100)

#惩罚值
def punish():
    return -(y*np.log(yp+(1-yp)*promise)+(1-y)*np.log(1-yp+(yp)*promise))

#判等函数，用于把y变形
def equal(k,r):
    if k==r:
        return 1
    else:
        return 0


#训练失败，初始化
def reset():
    global g
    global lock
    global matrixes
    global learningrate
    global costw
    global cost
    global derivative
    global dataa
    global dataz
    global err
    global zzh

    #generate random matrixes
    matrixes=[]
    for s in range(len(sizeofmatrixes)):
        if s==0:
            matrixes.append(np.random.rand(n+1,sizeofmatrixes[s])*ranbias*2-ranbias)
        else:
            matrixes.append(np.random.rand(sizeofmatrixes[s-1]+1,sizeofmatrixes[s])*ranbias*2-ranbias)
    #for i in range(len(sizeofmatrixes)):
            #print(matrixes[i].shape)
    g=0
    lock=LOCK
    learningrate*=downrate
    costw=1e20
    cost=1e20
    dataa=[]
    dataz=[]
    derivative=[]
    err=[]
    zzh=[]

#正向传播
def forwardPropagation():
    global g
    global lock
    global matrixes
    global learningrate
    global costw
    global derivative
    global datas
    global dataa
    global dataz
    global err
    global zzh
    global yp
    
    for i in range(len(matrixes)):
        if i==0:
            #print("V------------------------------V")
            #print(np.dot(X,matrixes[i]))
            dataz.append(np.dot(X,matrixes[i]))
        else:
            #print("V-------------XXX--------------V")
            #print(np.dot(datas[i-1],matrixes[i]))
            TEMP=np.column_stack([[[1]]*m,dataa[-1]])
            dataz.append(np.dot(TEMP,matrixes[i]))
        dataa.append(logisic(dataz[-1]))
    yp=logisic(dataz[-1])
    #print("lol"+str(yp))
    #print(datas)
#计算代价函数
def calCost():
    global g
    global lock
    global matrixes
    global learningrate
    global costw
    global derivative
    global datas
    global err
    global zzh

    ctcost1=0
    ctcost2=0
    ctcost1=np.sum(punish()*punish())/m
    for i in range(len(matrixes)):
        ctcost2+=lamda*np.sum(matrixes[i]*matrixes[i])/m/2
    print("cost of errors:"+str("%.6f"%(ctcost1))+"  cost of matrixes:"+str("%.6f"%(ctcost2)))
    costw=ctcost1+ctcost2
#反向传播
def backPropagation():
    global g
    global lock
    global matrixes
    global learningrate
    global costw
    global derivative
    global datas
    global err
    global zzh
    global dataa
    global dataz

    #正则化代价
    for i in range(len(matrixes)):
        zzh.append(lamda*(matrixes[i]*matrixes[i]))
        #print(matrixes[i])
    #误差代价
    for i in range(len(matrixes)):
        nb=len(matrixes)-i-1
        if i==0:
            err.append(dataa[-1]-y)
        else:
            tmp0=err[-1].transpose()
            tmp1=np.dot(matrixes[nb+1],tmp0)  #err[-1]多了偏置项,但要用克隆删除
            tmp1=tmp1.transpose()
            tmp2=dataa[nb]*(1-dataa[nb])
            #print("--------\n"+str(tmp2)+"\n--------\n")
            #print("("+str(tmp1.shape)+","+str(tmp2.shape)+")")
            tmp3=tmp1*np.column_stack([[[1]]*m,tmp2]) 
            tmp4=np.delete(tmp3,0,axis=1)
            err.append(tmp4)
    err.reverse()
    #for i in range(len(err)):
        #print(err[i].shape)
    #误差与正则化相加求出导数
    for i in range(len(dataa)):
        #print(i)
        if i!=0:
            #print(np.shape(lamda*zzh[nb]))
            derivative.append(zzh[i]+np.dot(err[i].transpose(),logisic(dataa[i-1])).transpose())
        else:
            derivative.append(zzh[nb]+np.dot(err[i].transpose(),X).transpose())
    #修改矩阵的值
    for i in range(len(matrixes)):
        matrixes[i]-=(learningrate*derivative[i])

#main function

#数据读取流开启
fpr1=open('TrainingExamples.txt','r')
fpr2=open('setter.txt','r')

#数据定义
m,n,c=0,0,0
X=[]
y=[]
matrixes=[]

dataa=[]
dataz=[]
derivative=[]
err=[]
zzh=[]
derivative=[]

#原始数据读入
fpr1.readline()
m,n,c=tuple([int(i) for i in (fpr1.readline()).split()])
for i in range(m):
    chart=[float(i) for i in (fpr1.readline()).split()]
    y.append(chart[-1])
    del chart[-1]
    TMP=[1]
    TMP.extend(chart)
    X.append(TMP)

sizeofmatrixes=[int(i) for i in (fpr2.readline()).split()]
sizeofmatrixes.append(c)
ranbias=float(fpr2.readline())

#关闭读取流
fpr1.close()
fpr2.close()

#原始数据设定
X=np.array(X)
yc=[]
for r in range(c):
    yc.append([equal(k,r) for k in y])
    yc[r]=np.array(yc[r])
y=np.array(yc)
y=y.transpose()

#测试设定是否正确
#print(X)
#print(y)
#print('m:%d\nn:%d\n'%(m,n))
#print('bias:%d\n'%(ranbias))
#print("sizeofmatrixes:"+sizeofmatrixes)
#input("输入回车继续\n")

#打开写入流
fpw1=open('recordcost.txt','w')
fpw2=open('result.txt','w')
fpw3=open('recordmatrixes.txt','w')

#输入信息
fpw3.writelines('m:%d\nn:%d\n'%(m,n))
fpw3.writelines('bias:%d\n'%(ranbias))
fpw3.writelines('layers:%d\n'%(len(sizeofmatrixes)))
fpw3.writelines(str(sizeofmatrixes))

#关键运算部分
fpw1.writelines("Now learning rate:%.6lf\n"%learningrate)
reset()
g=1
while g<=generation:
    #print(cost)
    #print(costw)
    forwardPropagation()
    calCost()
    backPropagation()
    fpw1.writelines("cost[%d] is %.6f\n"%(g,cost))
    if costw==np.nan or cost<costw:
        lock-=1
        fpw1.writelines("Error on generation %d\n"%(g+1))
    if lock==UNLOCK or costw>1e20:
        fpw1.writelines("----------------------------------")
        fpw1.writelines("Failed in generation %d\n"%(g+1))
        fpw1.writelines("Now learning rate:%.6lf\n"%learningrate);
        reset()
        continue
    cost=costw
    costw=0
    
    dataa=[]
    dataz=[]
    derivative=[]
    err=[]
    zzh=[]
    g+=1
fpw1.writelines("\n")
for i in range(len(matrixes)):
    fpw2.writelines(str(matrixes[i].shape)+"\n"+str(matrixes[i]))
fpw2.writelines("\n")
fpw1.writelines("terminated.\n")
fpw1.writelines(str(np.column_stack([y,yp]))+'\n')
fpw1.close()
fpw2.close()
fpw3.close()