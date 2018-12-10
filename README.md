# backmountain
Classification server based on scikit-learn

主要目的：
1，用同一套算法，根据不同的数据集训练不同的模型。
2，提供api接口，方便被调用。

思路：
1，dataset代表数据集。
    里面包含一个ds.json，描述数据集的信息。
    data.json，训练用的数据集。
    训练结果会生成一个model文件。
    
2，原则上，训练用机器和生产机器是不同的机器，所以训练用GPU，最终模型用CPU。

