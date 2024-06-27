卷积神经网络通常包含卷积层、池化层、正则层、激活层和上下采样层。这里我们逐步计算每一个层所需的参数量和FLOPs。  
> 其中，FLOPs和FLOPS的区别：FLOPS是处理器性能的衡量指标，是“每秒所执行的浮点运算次数”的缩写，而FLOPs是算法复杂度的衡量指标，是“浮点运算次数”的缩写，s代表的是复数。  
参数量与FLOPs分别可以反映模型的空间复杂度和时间复杂度。
> $参数量\approx计算量 \times H_{out} \times W_{out}$  
以下计算默认都有bias。
## 卷积层
参数量：
```math
Params = (k_H \times k_W \times C_{in}+1) \times C_{out}
```
计算量：
```math
FLOPs = 2 \times k_H \times k_W \times C_{in} \times C_{out} \times H_{out} \times W_{out}
```
## 全连接层
参数量：
```math
Params = (C_{in} + 1) \times C_{out}
```
计算量：
```math
FLOPs = 2 \times C_{in} \times C_{out}
```

## 归一化层（以Batch Normalization为例）
参数量：
```math
Params = 4 \times C_{out}
```
计算量：
```math
FLOPs = 2 \times C_{out} \times M_{outh} \times M_{outw}
```
FLOPs为2乘以输出通道数、输入的尺寸。

## 激活层（以Sigmoid为例）
参数量：没有超参数  
计算量：输入多少数，则计算多少次指数运算和多少次加法运算

## 池化层（以平均池化为例）
参数量：没有超参数  
计算量：
```math
FLOPs = H_{out} \times W_{out} \times C_{out} \times k_H \times k_W
```

![image](https://github.com/iamstarlee/Ubuntu-Tricks/assets/44799727/9399914e-b71a-4051-a9e5-69be48cc1bb1)

## References
1. [CNN中模型的参数量与FLOPs计算](https://paddlepedia.readthedocs.io/en/latest/tutorials/CNN/ParamsCounter.html)
2. [神经网络中常用算子参数量和计算量估计](https://qiyueliuhuo.github.io/posts/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E4%B8%AD%E5%B8%B8%E7%94%A8%E7%AE%97%E5%AD%90%E5%8F%82%E6%95%B0%E9%87%8F%E5%92%8C%E8%AE%A1%E7%AE%97%E9%87%8F%E4%BC%B0%E8%AE%A1/)
3. [一文讲解thop库计算FLOPs问题](https://blog.csdn.net/shuaijieer/article/details/129123379)
4. [YOLOX讲解](https://blog.csdn.net/weixin_43981952/article/details/122543820)
