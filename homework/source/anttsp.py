# -*- coding: utf-8 -*-

import random

# 城市坐标
# 城市坐标
distance_x=[232,189,299,501,300,588,455,1,25,564,155,156,874,665,163,564,23,565,89,45,65,8,9,2,64,323,566,626,234,215,125,154,326,975,962,953,862,845,862,846,729,168,423,658,2,89,78,46,43,18]
distance_y=[2,23,25,896,56,128,158,132,566,451,156,156,9,98,556,154,656,232,565,156,565,15,266,12,28,47,2,0,15,565,565,456,566,222,557,656,555,665,988,98,23,56,656,747,124,721,565,147,474,474]

distance=[[0 for i in range(50)]for i in range(50)]
#计算距离
i=0
while i<50:
    j=0
    while j<50:
        distance[i][j]=pow(distance_x[i]-distance_x[j],2)+pow(distance_y[i]-distance_y[j],2)
        distance[i][j]=pow(distance[i][j],0.5)
        j+=1
    i+=1
ant=[[]for i in range(50)]#key表示蚂蚁编号，value表示蚂蚁经过的城市
#蚂蚁走完一圈后的路径和
#信息素初始值为1
t=[[1 for i in range(50)]for i in range(50)]
#初始化蚂蚁位置
i=0
while i<50:
    ant[i].append(random.randint(0,49))
    i+=1
#信息素挥发速度
distancemin = 10000
pathmin=[]
pp=0.5
time=1
while time<10000:
    distance_ant = [0 for i in range(50)]
    city=0
    while city<49:
        num=0
        for key in ant:
            pd=0
            nextcity=0
            i=0
            while i<50:
                if i not in key:
                    p=t[key[-1]][i]/pow(distance[key[-1]][i],2)
                    if p>pd:
                        pd=p
                        nextcity=i
                i+=1
            distance_ant[num]+=distance[key[-1]][nextcity]
            key.append(nextcity)
            num+=1
        city+=1
    i=0
    for key in ant:
        key.append(key[0])
        distance_ant[i]+=distance[key[-1]][key[-2]]
        if distance_ant[i]<distancemin:
            distancemin=distance_ant[i]
            pathmin=ant[i]
        i+=1
    print('最短距离',distancemin,'迭代次数',time,'路径',pathmin)
    #信息素更新
    tchange = [[0 for i in range(50)] for i in range(50)]
    j=0
    for key in ant:
        i=0
        while i<50:
            tchange[key[i]][key[i+1]]+=(100/distance_ant[j])
            i+=1
        j+=1
    i=0
    while i < 50:
        j = 0
        while j < 50:
            t[i][j] = 0.5 * t[i][j]+tchange[i][j]+tchange[j][i]
            j += 1
        i += 1
    for key in ant:
        i=1
        while i<51:
            del key[1]
            i+=1
    time+=1