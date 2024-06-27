卷积神经网络通常包含卷积层、池化层、正则层、激活层和上下采样层。这里我们逐步计算每一个层所需的参数量和FLOPs。  
> 其中，FLOPs和FLOPS的区别：FLOPS是处理器性能的衡量指标，是“每秒所执行的浮点运算次数”的缩写，而FLOPs是算法复杂度的衡量指标，是“浮点运算次数”的缩写，s代表的是复数。  
参数量与FLOPs分别可以反映模型的空间复杂度和时间复杂度。  
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
Params = C_{in} \times C_{out} + C_{out}
```
计算量：
```math
FLOPs = 2 \times C_{in} \times C_{out}
```

## 归一化层（Batch Normalization）
参数量：
```math
Params = 4 \times C_{out}
```
计算量：
```math
FLOPs = 2 \times C_out \times M_{outh} \times M_{outw}
```
FLOPs为2乘以输出通道数、输入的尺寸。

## 激活层
参数量：0
计算量：0

## 池化层
参数量：0
计算量：0

