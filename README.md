# Ubuntu-Tricks
## How to quick search issues involving yourselves.
在GitHub搜索中放入is:issue involves:my-username

## ffmpeg合并多个MP4视频
1. 新建一个ideo.txt文件，文件内容是需要合并的视频名称
```
file 'test.mp4'
file 'test2.mp4'
```
2. 执行ffmpeg指令
```
ffmpeg -f concat -i video.txt -c copy concat.mp4
```
