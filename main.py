from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

 # 从文件中读取测试图片集
imgsFile = open("testSet/train-images.idx3-ubyte", 'rb')
imgsFile.read(4)
readBuffer = imgsFile.read(4)
# 图片数量
length = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
print (length)
 # 图片尺寸
readBuffer = imgsFile.read(4)
rows = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
print (rows)
readBuffer = imgsFile.read(4)
cols = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
print (cols)
 # 生成图片数组，每个数组元素为28*28的一维数组
imgsTrainDataSet = []
for i in range(0,length):
    # print(i)
    rowData = []
    for j in range(0,rows):
        for k in range(0,cols):
            pixelBuffer = imgsFile.read(1)
            rowData.append(int.from_bytes(pixelBuffer, byteorder='big'))
    imgsTrainDataSet.append(rowData)
print("finish reading imgsDataSet")
 # 从文件中读取label集合
labelsFile = open("testSet/train-labels.idx1-ubyte", 'rb')
labelsFile.read(4)
readBuffer = labelsFile.read(4)
# label数量
length = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
print (length)
 # 生成label数组，每个数组元素为0~9的整数
labelsTrainDataSet = []
for i in range(0,length):
    labelBuffer = labelsFile.read(1)
    labelsTrainDataSet.append(int.from_bytes(labelBuffer, byteorder='big'))
print("finish reading labelsDataSet")


 # 从文件中读取测试图片集
imgsFile = open("testSet/t10k-images.idx3-ubyte", 'rb')
imgsFile.read(4)
readBuffer = imgsFile.read(4)
# 图片数量
length = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
print (length)
 # 图片尺寸
readBuffer = imgsFile.read(4)
rows = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
print (rows)
readBuffer = imgsFile.read(4)
cols = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
print (cols)
 # 生成图片数组，每个数组元素为28*28的一维数组
imgsTestDataSet = []
for i in range(0,length):
    # print(i)
    rowData = []
    for j in range(0,rows):
        for k in range(0,cols):
            pixelBuffer = imgsFile.read(1)
            rowData.append(int.from_bytes(pixelBuffer, byteorder='big'))
    imgsTestDataSet.append(rowData)
print("finish reading imgsTestDataSet")
 # 从文件中读取label集合
labelsFile = open("testSet/t10k-labels.idx1-ubyte", 'rb')
labelsFile.read(4)
readBuffer = labelsFile.read(4)
# label数量
length = readBuffer[0] * pow(16,6) + readBuffer[1] * pow(16,4) + readBuffer[2] * pow(16,2) + readBuffer[3];
print (length)
 # 生成label数组，每个数组元素为0~9的整数
labelsTestDataSet = []
for i in range(0,length):
    labelBuffer = labelsFile.read(1)
    labelsTestDataSet.append(int.from_bytes(labelBuffer, byteorder='big'))
print("finish reading labelsTestDataSet")

# 训练样本集 测试样本集 测试样本的标记 测试样本的标记
AB = AdaBoostClassifier(n_estimators=1000)
AB.fit(imgsTrainDataSet,labelsTrainDataSet)
predict_results=AB.predict(imgsTestDataSet)
print(accuracy_score(predict_results, labelsTestDataSet))
conf_mat = confusion_matrix(labelsTestDataSet, predict_results)
print(conf_mat)
print(classification_report(labelsTestDataSet, predict_results))
