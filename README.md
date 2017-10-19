# datamining_algorithms
用python实现数据挖掘领域十大经典算法  
  
  
  ![image](http://s16.sinaimg.cn/middle/551d7bffg80cbb284ca7f&690)

## 2. K-Means  
### 简介  
又叫K-均值算法，是非监督学习中的聚类算法。  
### 基本思想  
在k-means算法中，用质心来表示cluster；且容易证明k-means算法收敛等同于所有质心不再发生变化。基本的k-means算法流程如下：
选取k个初始质心（作为初始cluster）；  
    <blockquote><p>**repeat**：</p>
       <p>对每个样本点，计算得到距其最近的质心，将其类别标为该质心所对应的cluster；</p>
       <p>重新计算k个cluser对应的质心；</p>
    **until** 质心不再发生变化</blockquote>
### 算法复杂度  
### 缺点

## 相关术语
                
**监督学习**(wipipedia)（英语：Supervised learning），是一个机器学习中的方法，可以由训练资料中学到或建立一个模式（函数 / learning model），并依此模式推测新的实例。训练资料是由输入物件（通常是向量）和预期输出所组成。函数的输出可以是一个连续的值（称为回归分析），或是预测一个分类标签（称作分类）。  
                                                           
**非监督学习**(wipipedia)是一种机器学习的方式，并不需要人力来输入标签。它是监督式学习和强化学习等策略之外的一种选择。在监督式学习中，典型的任务是分类和回归分析，且需要使用到人工预先准备好的范例(base)。
