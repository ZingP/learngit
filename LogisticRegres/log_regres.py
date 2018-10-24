from numpy import *


# 创建数据集 [[1.0, -0.017612, 14.053064],]  [0, 1, ...]
def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inX):
    return 1.0/(1+exp(-inX))


def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)  # 转换为numpy矩阵
    labelMat = mat(classLabels).transpose()  # 转换为numpy矩阵,列向量
    m, n = shape(dataMatrix)    # 100行 3列
    print(m, n)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))
    # 这几部没看懂啊
    for k in range(maxCycles):  # 矩阵运算
        print("K", k)
        h = sigmoid(dataMatrix*weights)  # matrix mult
        print("h:", h)
        error = (labelMat - h)  # vector subtraction
        print("error:", error)
        weights = weights + alpha * dataMatrix.transpose() * error  # matrix mult
        print("weight:", weights)
        input("niubi....")
    return weights


def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


if __name__ == '__main__':
    data_set, label_mat = loadDataSet()
    w = gradAscent(data_set, label_mat)
    plotBestFit(w.getA())
