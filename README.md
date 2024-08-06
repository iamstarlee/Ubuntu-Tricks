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
