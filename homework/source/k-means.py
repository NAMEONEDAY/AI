# -*- coding: utf-8 -*-

import cv2
import dlib
import numpy
import os
import glob

def getFace():
    # 加载人脸检测器，人脸模型，人脸特征点构建模型
    detector = dlib.get_frontal_face_detector()
    facerec = dlib.face_recognition_model_v1("2.dat")
    predictor = dlib.shape_predictor("1.dat")
    i=1
    dic={}
    for f in glob.glob(os.path.join('./face', "*.jpg")):
        image = cv2.imread(f)#读取图片
        dets = detector(image, 1)#人脸检测
        for k, d in enumerate(dets):
            # 2.关键点检测
            shape = predictor(image, d)
            # 3.描述子提取，128D向量
            u_1 = facerec.compute_face_descriptor(image, shape)#形成向量
        u=numpy.array(u_1)
        dic[i]=u#将向量加入到字典中
        i+=1
    return dic

def kmeans(s,dic):#
    s1=[[],[],[]]#初始化二维列表
    s.sort()#将原来的簇排序
    t=0
    mid={}#存放簇均值的字典
    for i in s:#计算簇均值
        t+=1
        m=0
        cc = numpy.zeros(128)
        for c in i:
            cc+=dic[c]
            m+=1
        cc=[x/m for x in cc]
        mid[t]=cc#将簇的均值存放到字典中
    t=0
    distance=numpy.zeros(4)#存放距离的数组
    for key1 in dic.keys():#对于所有的数据
        t+=1
        for i in mid.keys():#计算与三个簇均值的距离
            distance[i]=numpy.linalg.norm(dic[key1] - mid[i])#欧几里得距离
        h=1
        mind=1000
        minh=0
        while(h<4):#选取距离最小的簇
            if distance[h]<mind:
                minh=h-1
                mind=distance[h]
            h+=1
        s1[minh].append(key1)#加入到距离最小的簇中
    s1.sort()#将形成的新的三个簇排序
    if s==s1:#如果和原来的簇相等停止递归
        return s1
    else:#否则再次迭代
        return kmeans(s1,dic)

if __name__ == '__main__':
    dic=getFace()#获得人脸字典
    s=[[11],[12],[13]]#选取初始簇
    s=kmeans(s,dic)#k-均值聚类
    print(s)#输出
