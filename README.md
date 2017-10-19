# datamining_algorithms
用python3实现数据挖掘领域十大经典算法。十大经典算法如下：  
  
  
  ![image](http://s16.sinaimg.cn/middle/551d7bffg80cbb284ca7f&690)
           
>## <a href="#c4.5">1. C4.5</a>
>## <a href="#kmeans">2. K-Means</a>
>## <a href="#svm">3. SVM</a>
>## <a href="#apriori">4. Apriori</a>
>## <a href="#em">5. EM</a>
>## <a href="#pagerank">6. PageRank</a>
>## <a href="#adaboost">7. AdaBoost</a>
>## <a href="#knn">8. kNN</a>
>## <a href="#naïve bayes">9. Naïve Bayes</a>
>## <a href="#cart">10. CART</a>
>## <a href="#relation">相关术语</a>
      
       
         

## <a name="kmeans">2. K-Means</a>
### **简介**  
又叫K-均值算法，是非监督学习中的聚类算法。  
### **基本思想**  
在k-means算法中，用cluster来表示簇；且容易证明k-means算法收敛等同于所有质心不再发生变化。基本的k-means算法流程如下：

<blockquote>选取k个初始质心（作为初始cluster，每个初始cluster只包含一个点）；  
    **repeat**：  
    &nbsp;&nbsp;&nbsp;&nbsp;对每个样本点，计算得到距其最近的质心，将其类别标为该质心所对应的cluster；  
    &nbsp;&nbsp;&nbsp;&nbsp;重新计算k个cluster对应的质心（质心是cluster中样本点的均值）；  
    **until** 质心不再发生变化</blockquote>  

repeat的次数决定了算法的迭代次数。实际上，k-means的本质是最小化目标函数，目标函数为每个点到其簇质心的距离的平方和：
>![image](http://img.blog.csdn.net/20140419234515937)  

N是元素个数，x表示元素，c(j)表示第j簇的质心

### **算法复杂度**  
时间复杂度是O(nkt) ,其中n代表元素个数，t代表算法迭代的次数，k代表簇的数目

### **优缺点**  
**优点**
1. 简单、快速
2. 对大数据集有较高的效率并且是可伸缩性的
3. 时间复杂度近于线性，适合挖掘大规模数据集

**缺点**
1. k-means是局部最优，因而对初始质心的选取敏感
2. 选择能达到目标函数最优的k值是非常困难的


## <a name="relation">相关术语</a>  
**监督学习**(wipipedia)（supervised learning）  
>是一个机器学习中的方法，可以由训练资料中学到或建立一个模式（函数 / learning model），并依此模式推测新的实例。训练资料是由输入物件（通常是向量）和预期输出所组成。函数的输出可以是一个连续的值（称为回归分析），或是预测一个分类标签（称作分类）。  
                      
**非监督学习**(wipipedia)（unsupervised learning）  
>是一种机器学习的方式，并不需要人力来输入标签。它是监督式学习和强化学习等策略之外的一种选择。在监督式学习中，典型的任务是分类和回归分析，且需要使用到人工预先准备好的范例(base)。