# Ubuntu-Tricks
<details>
<summary> How to quick search issues involving yourselves.</summary>
在GitHub搜索中放入is:issue involves:my-username
</details>

<details>
<summary> ffmpeg将多个MP4视频合并为一个 </summary>
1. 新建一个vdeos.txt文件，文件内容是需要合并的视频名称
2. 执行ffmpeg指令
  
```bash
file 'test.mp4'
file 'test2.mp4'

ffmpeg -f concat -i videos.txt -c copy concat.mp4
```

</details>

<details>
<summary> ffmpeg将多张图片合并为一个MP4 </summary>

```
ffmpeg -f image2 -i %d.jpeg output.mp4
```
</details>

ffmpeg将视频调整成目标帧率
ffmpeg -i input1.mp4 -r 30 -vf "fps=30" temp1.mp4
其中，-r 30 指定目标帧率为 30 帧每秒，并使用 -vf "fps=30" 过滤器确保输出视频的帧率为 30 帧每秒。
