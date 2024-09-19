## 53. 下划线在python中的用途
[Python 中下划线的 5 种含义](https://www.runoob.com/w3cnote/python-5-underline.html#:~:text=%E5%BD%93%E6%B6%89%E5%8F%8A%E5%88%B0%E5%8F%98%E9%87%8F%E5%92%8C,PEP%208%E4%B8%AD%E6%9C%89%E5%AE%9A%E4%B9%89%E3%80%82)

## 52. import os重命名
```bash
os.rename(old_file_path, new_file_path)
```

## 51. Half and Float dtype
Half means dtype = torch.float16
while,
Float means dtype = torch.float32

## 50. What does 'register_buffer' do ?
If you have parameters in your model, which should be saved and restored in the state_dict, but not trained by the optimizer, you should register them as buffers.

## 49. torch.to(device)
```bash
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
```
## 48. Windows 查看文件夹中的所有文件信息
```bash
dir /b 查看当前路径下的所有文件和文件夹
dir /b /s 还可以查看子目录下的文件
```

## 47 获取sequential的模组名字
```bash
module = Sequential()
names = module.__class__.__nmae__
```

## 46. git撤回撤回
查看log
```bash
git reflog
```
回到特定commit
```bash
git reset --hard commitid
```
or
```bash
git reset --hard HEAD@{2} # {}中表示的是结点的序号
```

## 45. git撤回
撤回commit
```bash
git reset --soft HEAD^
```
撤回add
```bash
git reset --hard HEAD^
```

## 44. zip and unzip in ubuntu
```bash
zip -r file.zip folder
unzip file.zip -d folder
```

## 43. 关闭anaconda自动激活base环境导致环境有俩括号
```bash
conda config --set auto_activate_base false
```
![image](https://github.com/user-attachments/assets/2f38c918-a877-4ac5-bde9-c66e14493228)
![image](https://github.com/user-attachments/assets/a33231e9-e9ba-4afd-ade1-198e3a1d8851)


## 42. Ubuntu环境配置
1. wget安装anaconda3
```bash
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh
bash Anaconda3-5.3.1-Linux-x86_64.sh
```
2. pip安装torch2.3.0+cu121和torchvision0.18.0+cu121
```bash
pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu121
```

## 41. 查看内存和磁盘空间
```bash
free -m
df -h
```

## 40. 同时unzip多个zip文件
```bash
for file in train*.zip; do unzip "$file" -d /path/to/destination; done
```

## 39. 打印模型sequential的中间结果
```python
def printInfo(self):
    x = torch.rand([3,512,1,1])
    for name, module in self.fc.named_children():
        x = module(x)
        if isinstance(module,nn.Upsample):
            print("Upsample({}) : {}".format(name,x.shape))
        elif isinstance(module,nn.Conv2d):
            print("Conv2d({}) : {}".format(name,x.shape))

```

## 38. Ubuntu 查看源
```bash
cat /etc/apt/sources.list
```
cat（英文全拼：concatenate）命令用于连接文件并打印到标准输出设备上，它的主要作用是用于查看和连接文件。

## 37. Windows tricks 设置开机自启
1. Win + r
2. shell:startup
3. 把快捷方式拖进来

## 36 创建软连接和删除软连接！
```bash
ln -sf ../COCO/coco-pose ./dataset/coco-pose (后面dataset里面没有coco-pose，软连接会从前面链接一个coco-pose过来)
```
```bash
unlink ./dataset/coco-pose #最好不用rm删
```

## 35. 激活灵汐
```bash
source lyngor1.17/bin/activate
```

## 34. Windows与Linux系统在同一个局域网下互传文件
```bash
# 复制 Windows 文件到 Linux
scp D:\data\1.txt root@192.168.88.161:/root/data
# 复制 Windows 目录到 Linux（记得加 -r）
scp -r D:\data root@192.168.88.161:/root/data
 
# 复制 Linux 文件到 Windows
scp root@192.168.88.161:/root/data/1.txt D:\data
# 复制 Linux 目录到 Windows（记得加 -r）
scp -r root@192.168.88.161:/root/data D:\data
```

## 33. Look for version of Jetson Xavier NX
```bash
sudo apt-cache show nvidia-jetpack
```

## 32. Openpose
[Webcam](https://medium.com/pixel-wise/real-time-pose-estimation-in-webcam-using-openpose-python-2-3-opencv-91af0372c31c)

## 31. 多线程编译
```bash
make -j`nproc`
```

## 30. 用清华源下载特定包或者一定范围的包
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  " pyqtwebengine&lt<5.13"
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  pathlib
```

## 29. Ubuntu终端的复制粘贴
```bash
Ctrl + Shift + C
Ctrl + Shift + V
```

## 28. ubuntu安装卸载软件
```bash
sudo dpkg -i xxx.deb
sudo dpkg -r xxx
```

## 27. 安装缺少依赖
```bash
sudo apt-get -f install
```

## 26. numpy setting
```python
import numpy as np

# 保证所有数据能够显示，而不是用省略号表示，np.inf表示一个足够大的数
np.set_printoptions(threshold = np.inf) 

# 若想不以科学计数显示:
np.set_printoptions(suppress = True)

```

## 25. off-the-shelf

<center>
    <img src="https://github.com/user-attachments/assets/9bb4d2cb-37b0-4842-8de1-2bb979fe94ba" alt="example">
</center>

## 24. [Feature Selection Techniques in Machine Learning](https://www.analyticsvidhya.com/blog/2020/10/feature-selection-techniques-in-machine-learning/)

## 23. [How does nn.Embedding work?](https://discuss.pytorch.org/t/how-does-nn-embedding-work/88518)
关于torch.nn.Embedding通透的解释

## 22. Use `nproc` to know the number of cpu cores, or use `make -j${nproc}`

## 21. Ubuntu下的文件解压
```bash
tar -xvJf xxx.tar.xz
```
```bash
tar -zxvf xxx.tgz
```

## 20. [Onnxruntime c++ with CUDA](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html)

## 19. Ubuntu配置软链接
```bash
sudo ln -s /cuda/cuda118 /usr/local/cuda
```

## 18. Ubuntu文件或文件夹有锁
```bash
sudo chmod -R 777 文件夹或文件的路径
```

## 17. 将远端仓库同步到本地：git fetch + git merge == git pull

## 16. [Nvidia-CUDA Onnxruntime using c++](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html#cc)

## 15. [ONNX的算子列表](https://github.com/onnx/onnx/blob/f2daca5e9b9315a2034da61c662d2a7ac28a9488/docs/Operators.md)

## 14. [Nvidia-Docker的国内镜像地址](https://gitlab.com/nvidia/container-images/cuda/blob/master/doc/supported-tags.md)

## 13. How can I find out my user name?
```bash
whoami
```

## 12. [在服务器的docker里 装anacond3深度学习环境的全流程超基础](https://www.cnblogs.com/xiaoli1996/p/15959469.html)

## 11. Good tutorial to install opencv in Ubuntu
[Ubuntu 20.04搭建OpenCV 4.5.0 & C++环境](https://blog.csdn.net/weixin_44796670/article/details/115900538)

## 10. Cool profiles of Github
1. [如何拥有一款有特色的 Github Profile？](https://cloud.tencent.com/developer/article/2047199)
2. [Github 首页美化教程 —— 美，是第一生产力](https://blog.csdn.net/weixin_50915462/article/details/119988939)
3. [GitHub美化主页设计（保姆教程 && Markdown表情）](https://blog.csdn.net/qq_44231797/article/details/129251980)

## 9. What does 'register_buffer' do in pytorch ?
> If you have parameters in your model, which should be saved and restored in the state_dict, but not trained by the optimizer, you should register them as buffers.
Buffers won’t be returned in model.parameters(), so that the optimizer won’t have a change to update them.

## 8. pip下载指定镜像地址，或者直接设置清华源
```bash
pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple
```
```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 7. python导入其他文件夹中的包
最好加在文件中的第一行
```
import sys
sys.path.append('/path/to/your/module')
```

## 6.5
<details>
<summary> How to quick search issues involving yourselves.</summary>
在GitHub搜索中放入is:issue involves:my-username
</details>


## 6. ffmpeg将多个MP4视频合并为一个 
1. 新建一个vdeos.txt文件，文件内容是需要合并的视频名称
2. 执行ffmpeg指令
  
```bash
file 'test.mp4'
file 'test2.mp4'

ffmpeg -f concat -i videos.txt -c copy concat.mp4
```



## 5. ffmpeg将多张图片合并为一个MP4
```
ffmpeg -f image2 -i %d.jpeg output.mp4
```


## 4. ffmpeg将视频调整成目标帧率
> ffmpeg -i input1.mp4 -r 30 -vf "fps=30" temp1.mp4
其中，-r 30 指定目标帧率为 30 帧每秒，并使用 -vf "fps=30" 过滤器确保输出视频的帧率为 30 帧每秒。

## 3. Sublime 配置 C++11
[Sublime config C++](https://www.geeksforgeeks.org/setting-up-sublime-text-for-competitive-coding-in-cpp14-on-ubuntu/)

## 2. ViT：使用HuggingFace和Pytorch对Vision Transformer进行微调实战
[微调ViT的教程](https://blog.csdn.net/weixin_38739735/article/details/137064991)

## 1. 关于Ubuntu的使用细节

查看幻灯片的播放速度
```python
gsettings get org.yorba.shotwell.preferences.slideshow delay
gsettings get org.yorba.shotwell.preferences.slideshow show-title
gsettings get org.yorba.shotwell.preferences.slideshow transition-delay
```
修改幻灯片的播放速度
```python
gsettings set org.yorba.shotwell.preferences.slideshow delay 1
gsettings set org.yorba.shotwell.preferences.slideshow show-title true
gsettings set org.yorba.shotwell.preferences.slideshow transition-delay 0.1
```

## 0. Conda激活失效
```
source ~/anaconda3/etc/profile.d/conda.sh
```
