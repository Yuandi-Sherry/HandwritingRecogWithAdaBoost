from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import cv2
import numpy as np

 # 从文件中读取测试图片集
def readImgsFile(filename):
    # 打开文件
    imgsFile = open(filename, 'rb')
    imgsFile.read(4)
    readBuffer = imgsFile.read(4)
    # 图片数量
    length = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
    print (length)
     # 图片尺寸
    readBuffer = imgsFile.read(4)
    rows = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
    readBuffer = imgsFile.read(4)
    cols = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
     # 生成图片数组，每个数组元素为28*28的一维数组
    imgsTrainDataSet = []
    for i in range(0,length):
        rowData = []
        for j in range(0,rows):
            for k in range(0,cols):
                pixelBuffer = imgsFile.read(1)
                rowData.append(int.from_bytes(pixelBuffer, byteorder='big'))
        imgsTrainDataSet.append(rowData)
    print("finish reading imgsDataSet")
    return imgsTrainDataSet

 # 从文件中读取label集合
def readLabelsFile(filename):
    labelsFile = open(filename, 'rb')
    labelsFile.read(4)
    readBuffer = labelsFile.read(4)
    # label数量
    length = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
    print (length)
     # 生成label数组，每个数组元素为0~9的整数
    labelsTrainDataSet =[[] for i in range(10)]
    for i in range(0,length):
        labelBuffer = labelsFile.read(1)
        for j in range(0,10):
            labelsTrainDataSet[j].append(-1)
        # print(int.from_bytes(labelBuffer, byteorder='big'))
        labelsTrainDataSet[int.from_bytes(labelBuffer, byteorder='big')][i] = 1
    print("finish reading labelsDataSet")
    return labelsTrainDataSet

 # 从文件中读取labelTest集合
def readLabelsTestFile(filename):
    labelsFile = open(filename, 'rb')
    labelsFile.read(4)
    readBuffer = labelsFile.read(4)
    # label数量
    length = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
    print (length)
     # 生成label数组，每个数组元素为0~9的整数
    labelsTestDataSet =[]
    for i in range(0,length):
        labelBuffer = labelsFile.read(1)
        labelsTestDataSet.append(int.from_bytes(labelBuffer, byteorder='big'))
    print("finish reading labelsDataSet")
    return labelsTestDataSet

if __name__ == '__main__':
    ImgsTrainData = readImgsFile("testSet/train-images.idx3-ubyte")
    labelsTrainData = readLabelsFile("testSet/train-labels.idx1-ubyte")
    ImgsTestData = readImgsFile("testSet/t10k-images.idx3-ubyte")
    labelsTestData = readLabelsTestFile("testSet/t10k-labels.idx1-ubyte")
    # 训练样本集 测试样本集 测试样本的标记 测试样本的标记
    # 训练分类器0
    AB = [AdaBoostClassifier(n_estimators=100) for i in range(10)]
    predict_results = [[[]for j in range(10)] for i in range(len(labelsTestData))]
    resultLabel = [[] for i in range(len(labelsTestData))]
    for i in range(10):
        AB[i].fit(ImgsTrainData,labelsTrainData[i])
        # 对测试集的每个元素进行预测
        for j in range(len(labelsTestData)):
            temp = []
            temp.append(ImgsTestData[j])
            # print(temp)
            predict_results[j][i]=AB[i].predict_proba(temp)[0][1]

    for i in range(len(labelsTestData)):
        resultLabel[i] = predict_results[i].index(max(predict_results[i]))

    print(accuracy_score(resultLabel, labelsTestData))
    conf_mat = confusion_matrix(labelsTestData, resultLabel)
    print(conf_mat)
    print(classification_report(labelsTestData, resultLabel))
