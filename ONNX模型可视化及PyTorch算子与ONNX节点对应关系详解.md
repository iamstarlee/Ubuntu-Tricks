1. 矩阵的切片操作。
在ONNX中，矩阵切片操作如tensor[0:, :, 0:2]会被转换为Slice节点。Slice节点会显示出起始索引、结束索引和步长等参数，从而实现了对矩阵的切片操作。
![image](https://github.com/iamstarlee/Ubuntu-Tricks/assets/44799727/f855a4c3-1a5e-4301-a2c7-ddbb653d474a)
