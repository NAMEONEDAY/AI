# -*- coding: utf-8 -*-

import random

# 城市坐标
distance_x = [
    178,272,176,171,650,499,267,703,408,437,491,74,532,
    416,626,42,271,359,163,508,229,576,147,560,35,714,
    757,517,64,314,675,690,391,628,87,240,705,699,258,
    428,614,36,360,482,666,597,209,201,492,294]
distance_y = [
    170,395,198,151,242,556,57,401,305,421,267,105,525,
    381,244,330,395,169,141,380,153,442,528,329,232,48,
    498,265,343,120,165,50,433,63,491,275,348,222,288,
    490,213,524,244,114,104,552,70,425,227,331]



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
ant = [[] for i in range(50)]  # key表示蚂蚁编号，value表示蚂蚁经过的城市
# 初始化蚂蚁位置
i = 0
while i < 50:
    ant[i].append(random.randint(0, 49))
    i += 1
#信息素初始值为1
t=[[1.0 for i in range(50)]for i in range(50)]
distancemin = 10000
pathmin=[]
time=1
while time<10000:
    # 蚂蚁走完一圈后的路径和
    distance_ant = [0 for i in range(50)]
    i=0
    for key in ant:
        num = 0  # 已经走过的城市个数
        while num < 49:
            city = 0
            p = [0 for i in range(50)]
            pall=0
            nextcity = -1  # 下一个城市的编号
            while city < 50:
                if city not in key:  # 如果这个蚂蚁没有走过这个城市
                    p[city] = pow(t[key[-1]][city],1) * pow(1 / distance[key[-1]][city], 2.0)  # 计算概率t为信息素浓度，distance为两个城市距离
                    pall+=p[city]
                city+=1
            # 轮盘选择城市
            if pall > 0:
                # 产生一个随机概率
                temp_prob = random.uniform(0.0, pall)
                for j in range(50):
                    if j not in key:
                        # 轮次相减
                        temp_prob -= p[j]
                        if temp_prob < 0.0:
                            nextcity = j
                            break

            # 未从概率产生，顺序选择一个未访问城市
            if nextcity == -1:
                for j in range(50):
                    if j not in key:
                        nextcity = j
                        break
            distance_ant[i] += distance[key[-1]][nextcity]  # 计算当前走过的距离
            key.append(nextcity)  # 将这个城市加入到已经走过的城市中去
            num += 1
        i+=1
    i=0
    for key in ant:
        key.append(key[0])#将初始城市加入到列表末尾
        distance_ant[i]+=distance[key[-1]][key[-2]]#加上回到初始城市的距离
        if distance_ant[i]<distancemin:#找到最优的城市
            distancemin=distance_ant[i]
            pathmin=ant[i]
            minant=i
        i+=1
    print('最短距离',distancemin,'迭代次数',time,'路径',pathmin)
    #信息素更新
    tchange = [[0 for i in range(50)] for i in range(50)]
    j=0
    for key in ant:#根据蚂蚁走过的城市增加信息素为100/蚂蚁走过的总距离
        i=0
        while i<50:
            tchange[key[i]][key[i+1]]+=(100.0/distance_ant[j])
            tchange[key[i+1]][key[i]]=tchange[key[i]][key[i+1]]
            i+=1
        j+=1

    i=0
    while i < 50:#每条路径更新信息素为0.5*原信息素浓度+增加信息素浓度
        j = 0
        while j < 50:
            t[i][j] = 0.5 * t[i][j]+tchange[i][j]
            j += 1
        i += 1
    for key in ant:#清空蚂蚁走过的城市
        i=0
        while i<50:
            del key[1]
            i+=1
    time+=1