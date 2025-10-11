## 73. ffmpeg 视频转图片
```bash
ffmpeg -i output.mp4 -vf "fps=30" output_images/image%04d.png
```

## 72. Chromium Downloading in Nvidia Jetson Orin Nx
```bash
sudo apt install chromium-browser
```

## 71. Word复选框打勾和打叉
```bash
数字2611 + (快捷键ALT+X)
数字2612 + (快捷键ALT+X)
```

## 70. Huggingface下载超时
```bash
You can solve this problem by setting the Hugging Face endpoint in the environment.
For example, in a Python script: os.environ["HF_ENDPOINT"] = "https://hf-mirror.com".
Or in the terminal: HF_ENDPOINT=https://hf-mirror.com python xxx.py.
Reference link: https://hf-mirror.com/
```

## 69. Ubuntu修改~/.config/pip/pip.conf或~/miniconda3/envs/pt39/pip.conf源
```python
pip config set global.index-url https://pypi.ngc.nvidia.com
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 68. git清理untrack文件
用该命令删除的文件无法找回，但如果git add过就不会被删掉。
参数说明：
- `n`:显示将要被删除的文件以及目录。
- `d`:删除未被添加到git路径中的文件以及目录（将.gitignore文件标记的文件全部删除）。
- `f`:强制执行（只会删除文件）。
- `x`:删除没有被track的文件。
```bash
//使用帮助文档 (git clean)
git help clean

//演习示范，提前告诉你那些文件会被删除，不会真正删除
git clean -n

//删除当前目录下所有没有track过的文件，.gitignore文件里指定的不会删除。
git clean -f

//删除指定路径下的没有被track过的文件
git clean -f <path>

//强制删除所有没有被track过的文件和文件夹，
git clean -df

//强制删除所有没有被track过的文件（.gitignore文件里指定的也不能避免）
git clean -fx

```

## 67. ssh与https之间的切换
```bash
# using https instead of ssh
git config --global url."https://github.com/".insteadOf git@github.com:
git config --global url."https://".insteadOf git://

# using ssh instead of https
git config --global url."git@github.com:".insteadOf https://github.com/
git config --global url."git://".insteadOf https://
```

## 66. 添加.gitignore文件可以忽略掉不想上传的更改
```bash
target          //忽略这个target目录
angular.json    //忽略这个angular.json文件
log/*           //忽略log下的所有文件
css/*.css       //忽略css目录下的.css文件
```

## 65. WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ProxyError('Cannot connect to proxy.', NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x7f891079f160>: Failed to establish a new connection: [Errno 111] 拒绝连接'))': /simple/ninja/
先
```python
export http_proxy=''
export https_proxy=''
```
后
```python
unset all_proxy
unset ALL_PROXY
```


## 64. 多卡推理
问：ValueError: Cannot assign non-leaf Tensor to parameter 'weight'. Model parameters must be created explicitly. To express 'weight' as a function of another Tensor, compute the value in the forward() method.  
答：指定一张显卡：CUDA_VISIBLE_DEVICES=0 python predict.py

## 63. !pip install -q xxx
```bash
-q: stands for 'quiet mode', which suppresses most of the output during installation.
!: This is used to run shell commands from within a Jupyter notebook.
```

## 62. nohup
```bash
tail -1000 nohup.out  (查看最后1000行日志文本）　
tail -ｆ nohup.out   （监控日志打印）
```
查看nohup.out最后1000行数据

## 61. 杀死stopped process
```bash
kill -9 `jobs -ps`
```
jobs -ps lists the process IDs (-p) of the stopped (-s) jobs.

## 60. 导出和安装anaconda环境
使用pip
```bash
pip freeze > requirements.txt
```
```bash
pip install -r requirements.txt
```
使用conda
```bash
conda env export > environment.yaml
```
```bash
conda env create -f environment.yaml
```

## 59 python print带颜色输出
```python
print("\n\033[1;33;44m温馨提示，head部分没有载入是正常现象，Backbone部分没有载入是错误的。\033[0m")
```
- \033 This is the escape character, which begins the ANSI color code sequence.
- 1 : This specifies bold text.
- 33 : This sets the text color to yellow.
- 44 : This sets the background color to blue.
- m : This marks the end of the color code and applies the style.
- \033[0m: This resets the color formatting back to the default after the message, ensuring that subsequent text is not affected by this style.

## 58. torch.where(condition, input, other)
根据判断条件选择替换元素  
Return a tensor of elements selected from either input or other, depending on condition.  
如果x的元素大于0，就替换为1.0，否则就替换为0.0
```python
torch.where(x > 0, 1.0, 0.0)
```

## 57. 环境变量的应用
在运行 Python 脚本的命令前加上环境变量设置，这样环境变量会应用于该次运行！
```python
CUDA_VISIBLE_DEVICE=0 python main.py
```

## 56. python格式化输出f-string
给所有keys值添加backbone前缀！
```python
renamed_dict = {f'backbone.{k}': v 
                for k, v in pretrained_dict.items()}
```

## 55. Linux查看进程
htop 是一个 Linux 下的交互式的进程浏览器，可以用来替换Linux下的top命令。
```bash
apt-get install htop
htop
```


## 54. Ubuntu统计文件夹内的文件数量
- 统计当前目录下文件的个数（不包括目录）
```bash
ls -l | grep "^-" | wc -l
```
- 统计当前目录下文件的个数（包括目录）
```bash
ls -lR | grep "^-" | wc -l
```
- 查看某目录下文件夹(目录)的个数（包括子目录）
```bash
ls -lR | grep "^d" | wc -l
```

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
见md文件

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
pip install torch==2.3.0+cu121 torchvision==0.18.0+cu121 torchaudio==2.3.0+cu121 --index-url https://download.pytorch.org/whl/cu121
```
```bash
pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1+cu118 -f https://download.pytorch.org/whl/torch_stable.html
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
## 36.5 python3软链接到python
```bash
ln -s /usr/bin/python3 /usr/bin/python
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

## 14. 国内NVIDIA镜像地址
1. [https://gitlab.com/nvidia/container-images/cuda/blob/master/doc/supported-tags.md](https://gitlab.com/nvidia/container-images/cuda/blob/master/doc/supported-tags.md)  
2. [https://docker.aityp.com/r/docker.io/nvidia/cuda](https://docker.aityp.com/r/docker.io/nvidia/cuda)

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
