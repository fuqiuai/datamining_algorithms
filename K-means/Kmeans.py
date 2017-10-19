from numpy import *
import matplotlib.pyplot as plt

def loadDataSet(fileName):
    '''
    加载测试数据集，返回一个列表，列表的元素是一个坐标
    '''
    dataList = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float,curLine))
        dataList.append(fltLine)
    return dataList

def distEclud(vecA, vecB):
    '''
    计算两个点的距离
    '''
    return sqrt(sum(power(vecA - vecB, 2)))

def randCent(dataSet, k):
    '''
    随机生成k个初始的质心
    '''
    n = shape(dataSet)[1] # n表示数据集的维度
    centroids = mat(zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = mat(minJ + rangeJ * random.rand(k,1))
    return centroids

def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    '''
    KMeans算法，返回最终的质心坐标和每个点所在的簇
    '''
    m = shape(dataSet)[0] # m表示数据集的长度（个数）
    clusterAssment = mat(zeros((m,2)))

    centroids = createCent(dataSet, k) # 保存k个初始质心的坐标
    clusterChanged = True
    iterIndex=1 # 迭代次数
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
            print("第%d次迭代后%d个质心的坐标:\n%s"%(iterIndex,k,centroids)) # 第一次迭代的质心坐标就是初始的质心坐标
            iterIndex+=1
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            centroids[cent,:] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment

def showCluster(dataSet, k, centroids, clusterAssment):
    '''
    数据可视化,只能画二维的图（若是三维的坐标图则直接返回1）
    '''
    numSamples, dim = dataSet.shape
    if dim != 2:
        return 1

    mark = ['or', 'ob', 'og', 'ok','oy','om','oc', '^r', '+r', 'sr', 'dr', '<r', 'pr']

    # draw all samples
    for i in range(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Pr', 'Pb', 'Pg', 'Pk','Py','Pm','Pc','^b', '+b', 'sb', 'db', '<b', 'pb']
    # draw the centroids
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)

    plt.show()


if __name__ == '__main__':

    dataMat = mat(loadDataSet('./testSet')) #mat是numpy中的函数，将列表转化成矩阵

    k = 4 # 选定k值，也就是簇的个数（可以指定为其他数）
    cent, clust = kMeans(dataMat, k)
    
    showCluster(dataMat, k, cent, clust)
