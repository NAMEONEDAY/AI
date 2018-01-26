# coding=utf-8
from math import log


# 计算熵的函数
def getShannonEnt(dataSet):
    numEntries = len(dataSet)#得到模型的大小
    labelCounts = {}#结果的词典
    for feaVec in dataSet:#对于模型中的每条数据
        currentLabel = feaVec[-1]
        if currentLabel not in labelCounts:
            labelCounts[currentLabel] = 0#如果是一个新的结果，将结果加入到字典的key中
        labelCounts[currentLabel] += 1#对应key的值+1
    shannonEnt = 0.0
    for key in labelCounts:#计算熵
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSet(dataSet, i, value):#dataset是原模型，i是属性的标号，value是具体的属性值
    DataSet = []
    for feat in dataSet:#对于每条模型，如果属性值相同，就加入到这个属性列表中去
        if feat[i] == value:
            Dataset1=feat[:i]
            Dataset1.extend(feat[i+1:])
            DataSet.append(Dataset1)
    return DataSet

def getBestFeature(dataSet):
    numFeats = len(dataSet[0]) - 1  # 获得数据模型中属性的个数
    baseEntropy = getShannonEnt(dataSet)#计算基本的熵
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeats):#对于模型中的每个属性
        featList = [example[i] for example in dataSet]#得到属性的所有属性值
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:#对于每个属性值计算出他的熵
            subDataSet = splitDataSet(dataSet, i, value)#得到这个属性值对应的模型
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * getShannonEnt(subDataSet)#相加得到这个属性的熵
        infoGain = baseEntropy - newEntropy#两个熵相减得到信息增益
        if infoGain > bestInfoGain:#比较信息增益得到信息增益最大的属性
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

#dataset是模型，labels是特征
def createTree(dataSet, labels):#创建树的函数
    resultList = [example[-1] for example in dataSet]#得到dataset最后一列的数据
    if resultList.count(resultList[0]) == len(resultList):  # 该节点下所有结果相同停止划分
        return resultList[0]
    bestFeat = getBestFeature(dataSet)#获得熵增加最多的特征
    bestFeatLabel = labels[bestFeat]#特征名称
    myTree = {bestFeatLabel: {}}#使用字典方式创建树
    del (labels[bestFeat])#删除被选为节点的特征
    featValues = [example[bestFeat] for example in dataSet]#得到选为节点的属性的属性值
    uniqueVals = set(featValues)
    for value in uniqueVals:#通过递归得到每个属性值下的树
        subLabels = labels[:]  # 为了不改变原始列表的内容复制了一下
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat, value), subLabels)#splitdataset是得到这个属性值下的所有模型的函数
    return myTree

def getresult(pathtree):#得到最终结果的函数
    for key in pathtree.keys():#从根节点开始询问
        print('how about the',key)
        value=input()
        value=int(value)#得到选择
        if pathtree[key][value]=='yes':#如果字典对应的值是'yes'或者'no'到达叶节点
            return 'yes'
        elif pathtree[key][value]=='no':
            return 'no'
        return getresult(pathtree[key][value])#否则的话看这个节点下面的树，递归得到应得的结果

if __name__ == '__main__':
    data = [[1, 1, 1, 1, 'no'],#初始化训练模型
            [1, 1, 1, 2, 'no'],
            [2, 1, 1, 1, 'yes'],
            [3, 2, 1, 1, 'yes'],
            [3, 3, 2, 1, 'yes'],
            [3, 3, 2, 2, 'no'],
            [2, 3, 2, 2, 'yes'],
            [1, 2, 1, 1, 'no'],
            [1, 3, 2, 1, 'yes'],
            [3, 2, 2, 1, 'yes'],
            [1, 2, 2, 2, 'yes'],
            [2, 2, 1, 2, 'yes'],
            [2, 1, 2, 1, 'yes'],
            [3, 2, 1, 2, 'yes']]
    labels = ['OUTLOOK', 'TEMPERATURE', 'HUNIDITY', 'WIND', 'PLAYTENNIS']#属性标签
    myTree = createTree(data, labels)#得到树
    print(myTree)#输出树的结构
    print('OUTLOOK:SUNNY-1 OVERCAST-2 RAIN-3')
    print('TEMPERATURE:HOT-1 MILD-2 COLL-3')
    print('HUMIDITY:HIGH-1 NORMAL-2')
    print('WIND:WEAK-1 STRONG-2')
    pathtree=myTree
    result=getresult(pathtree)#得到结果
    print(result)#输出结果

