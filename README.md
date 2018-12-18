# 利用sklearn的AdaBoost手写体数字识别

## 实验环境

- python 3.6.7
- opencv 3.4.4

**编译指令：**

```shell
# python3 main.py
```

## 实验内容

用Adaboost实现手写体数字的检测器；然后针对测试数据进行测试. 

## 实验过程

1. 读取MNIST数据集的训练（维度为28*28的一维数组）和测试数据（0~9的数字）
2. 将28*28个像素点作为每一个样本的特征
3. 调用AdaBoostClassifier对于训练图片集和测试集进行训练
4. 使用训练好的分类器对于输入的图片进行识别（输出0~9的label作为结果）

## 实验改进

由于AdaBoost算法对于多label的情况并不是很好，因而将一个10label的分类器变为10个2label{-1,1}的分类器。

> 这样做的代价在于需要训练10个分类器，会导致时间成本的浪费。但正确率却能显著提高。

在读入label的时候进行如下处理：

```python
for i in range(0,length):
    labelBuffer = labelsFile.read(1)
    for j in range(0,10):
        labelsTrainDataSet[j].append(-1)
    labelsTrainDataSet[int.from_bytes(labelBuffer, byteorder='big')][i] = 1
```

进行AdaBoost训练：

```python
for i in range(10):
    AB[i].fit(ImgsTrainData,labelsTrainData[i])
    # 对测试集的每个元素进行预测
    for j in range(len(labelsTestData)):
        temp = []
        temp.append(ImgsTestData[j])
        # print(temp)
        predict_results[j][i]=AB[i].predict_proba(temp)[0][1]
# 找到最大可能对应的label        
for i in range(len(labelsTestData)):
        resultLabel[i] = predict_results[i].index(max(predict_results[i]))
```

## 实验结果

### 改进前：

正确率：71%

![不进行二值化和特征提取，直接是使用像素点训练](C:\Users\Sherry\Documents\Junior\ComputerVision\Homework\作业7\test1\Question2\imgs\不进行二值化和特征提取，直接是使用像素点训练.PNG)

### 改进后：

正确率：88%