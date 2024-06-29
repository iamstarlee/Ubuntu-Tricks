# Ubuntu-Tricks

## Cool profiles of Github
1. [如何拥有一款有特色的 Github Profile？](https://cloud.tencent.com/developer/article/2047199)
2. [Github 首页美化教程 —— 美，是第一生产力](https://blog.csdn.net/weixin_50915462/article/details/119988939)
3. [GitHub美化主页设计（保姆教程 && Markdown表情）](https://blog.csdn.net/qq_44231797/article/details/129251980)

## What does 'register_buffer' do in pytorch ?
> If you have parameters in your model, which should be saved and restored in the state_dict, but not trained by the optimizer, you should register them as buffers.
Buffers won’t be returned in model.parameters(), so that the optimizer won’t have a change to update them.

## pip下载指定镜像地址，
```
pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## python导入其他文件夹中的包
最好加在文件中的第一行
```
import sys
sys.path.append('/path/to/your/module')
```


<details>
<summary> How to quick search issues involving yourselves.</summary>
在GitHub搜索中放入is:issue involves:my-username
</details>


## ffmpeg将多个MP4视频合并为一个 
1. 新建一个vdeos.txt文件，文件内容是需要合并的视频名称
2. 执行ffmpeg指令
  
```bash
file 'test.mp4'
file 'test2.mp4'

ffmpeg -f concat -i videos.txt -c copy concat.mp4
```



## ffmpeg将多张图片合并为一个MP4
```
ffmpeg -f image2 -i %d.jpeg output.mp4
```


## ffmpeg将视频调整成目标帧率
> ffmpeg -i input1.mp4 -r 30 -vf "fps=30" temp1.mp4
其中，-r 30 指定目标帧率为 30 帧每秒，并使用 -vf "fps=30" 过滤器确保输出视频的帧率为 30 帧每秒。

## Sublime 配置 C++11
[Sublime config C++](https://www.geeksforgeeks.org/setting-up-sublime-text-for-competitive-coding-in-cpp14-on-ubuntu/)

## ViT：使用HuggingFace和Pytorch对Vision Transformer进行微调实战
[微调ViT的教程](https://blog.csdn.net/weixin_38739735/article/details/137064991)

## 关于Ubuntu的使用细节

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

## Conda激活失效
```
source ~/anaconda3/etc/profile.d/conda.sh
```
