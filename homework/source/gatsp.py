# -*- coding: utf-8 -*-

import random
import operator

def mklife():
    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31, 32, 33, 34, 35, 36,37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    random.shuffle(seq)
    return seq

def jiaocha(a,b):
    e=[]
    for i in a:
        e.append(i)
    ci=random.randint(1,50)
    i=0
    while i<ci:
        e.append(b[i])
        i+=1
    c=[]
    i=49+ci
    while i>=0:
        if e[i] not in c:
            c.append(e[i])
        i-=1
    d=[]
    i = 49
    while i >= 0:
        if c[i] not in d:
            d.append(c[i])
        i -= 1
    return d

def tubian(a):
    i=random.randint(0,49)
    j=random.randint(0,49)
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp
    return a

def getdistance(s):
    gadistance=0.0
    j=0
    while j<49:
        gadistance+=distance[s[j]][s[j+1]]
        j+=1
    gadistance+=distance[s[0]][s[49]]
    return gadistance

def getfit(s):
    return 1/s

class GA:
    def __init__(self):
        self


if __name__ == "__main__":
    distance_x = [232, 189, 299, 501, 300, 588, 455, 1, 25, 564, 155, 156, 874, 665, 163, 564, 23, 565, 89, 45, 65, 8,
                  9, 2, 64, 323, 566, 626, 234, 215, 125, 154, 326, 975, 962, 953, 862, 845, 862, 846, 729, 168, 423,
                  658, 2, 89, 78, 46, 43, 18]
    distance_y = [2, 23, 25, 896, 56, 128, 158, 132, 566, 451, 156, 156, 9, 98, 556, 154, 656, 232, 565, 156, 565, 15,
                  266, 12, 28, 47, 2, 0, 15, 565, 565, 456, 566, 222, 557, 656, 555, 665, 988, 98, 23, 56, 656, 747,
                  124, 721, 565, 147, 474, 474]

    distance = [[0 for i in range(50)] for i in range(50)]
    distancemin=10000
    pathmin=[]
    # 计算距离
    i = 0
    while i < 50:
        j = 0
        while j < 50:
            distance[i][j] = pow(distance_x[i] - distance_x[j], 2) + pow(distance_y[i] - distance_y[j], 2)
            distance[i][j] = pow(distance[i][j], 0.5)
            j += 1
        i += 1


    ga=[GA() for i in range(50)]
    ganew=[GA() for i in range(50)]
    #生成初始群体
    for i in ga:
        i.list=mklife()
        i.gadistance=getdistance(i.list)
        i.fitt=getfit(i.gadistance)
    cmpfun=operator.attrgetter('gadistance')
    ga.sort(key=cmpfun)#按照距离的从小到大排序
    t=1
    while t<200000:
        #选择操作
        j=0
        while j<30:
            ganew[j].list=ga[j].list
            j+=1
        j = 0
        while j < 15:
            ganew[j+30].list = ga[j].list
            j += 1
        j = 0
        while j < 5:
            ganew[j+30+15].list = ga[j].list
            j += 1
        #交叉操作
        num=0
        while num<50:
            p=random.random()
            if p<0.7:
                i=random.randint(0,49)
                j=random.randint(0,49)
                ganew[num].list=jiaocha(ganew[i].list,ganew[j].list)
            num+=1
        # 突变操作
        num=0
        while num<50:
            p=random.random()
            if p<0.1:
                ganew[num].list=tubian(ganew[num].list)
            num += 1
        for i in ganew:
            i.gadistance = getdistance(i.list)
            i.fitt = getfit(i.gadistance)
        cmpfun = operator.attrgetter('gadistance')
        ganew.sort(key=cmpfun)
        if(ganew[0].gadistance<distancemin):
            distancemin=ganew[0].gadistance
            pathmin=ganew[0].list
        print('最短距离',distancemin,'迭代次数',t,'路径',pathmin)
        ga=ganew
        t+=1