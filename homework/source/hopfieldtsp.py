# -*- coding: utf-8 -*-
#n=4

import numpy
import math
import random

n=4
d=[[0,3,5,6],[3,0,4,3],[5,4,0,3],[6,3,5,0]]
h=[[-1,-1,1,-1],[-1,1,1,1],[1,1,-1,-1],[1,-1,1,1]]
l1=500
l2=500
l3=200
l4=300
w=[[[[0 for i in range(4)]for i in range(4)]for i in range(4)]for i in range(4)]
x=0
q=[[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0]]

while(x<4):
    y=0
    while(y<4):
        i=0
        while(i<4):
            j=0
            while(j<4):
                w[x][i][y][j]=-(l1*d[x][y]*(q[i][j+1]+q[i][j-1])+l2*q[x][y]*(1-q[x][y])+l3*q[i][j]*(1-q[x][y])+l4*(1-q[x][y])*(1-q[i][j]))
                j+=1
            i+=1
        y+=1
    x+=1


I=[[0 for i in range(4)]for i in range(4)]
x=0
while x<4:
    i=0
    while i<4:
        I[x][i]=l4*n
        i+=1
    x+=1

t=0
while t<100000:
    a=random.randint(0, 3)
    b=random.randint(0,3)
    s=0
    i=0
    while i<4:
        j=0
        while j<4:
            s+=w[a][b][i][j]*h[i][j]
            j+=1
        i+=1
    s+=I[a][b]
    if s>=0:
        h[a][b]=1
    else:
        h[a][b]=-1
    e=0
    x=0
    while x<4:
        i=0
        while i<4:
            y=0
            while y<4:
                j=0
                while j<4:
                    e-=0.5*h[x][i]*w[x][i][y][j]*h[y][j]
                    j+=1
                y+=1
            i+=1
        x+=1
    x=0
    while x<4:
        i=0
        while i<4:
            e-=0.5*I[x][i]*h[x][i]
            i+=1
        x+=1
    print ('神经元状态',h,'能量',e,'迭代次数',t)
    t+=1
