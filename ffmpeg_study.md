使用ffmpeg将图片拼接成视频前，需要将图片文件名做下预处理，文件名中必须有数字将其次序标记出来。

直接使用命令
```
ffmpeg -f image2 -i %d.jpeg output.mp4 
```
就可以将其转为mp4视频，命令中的%d是数字编号占位符，ffmpeg会按次序加载*.jpeg作为输入。这里没有指定其他参数，所以ffmpeg使用了默认的参数，比如帧率是25fps，视频使用了h264编码，分辨率直接使用了图片原始分辨率……
```
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'output.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf58.76.100
  Duration: 00:00:10.00, start: 0.000000, bitrate: 28144 kb/s
  Stream #0:0(und): Video: h264 (High) (avc1 / 0x31637661), yuvj420p(pc, bt470bg/unknown/unknown), 2816x2160 [SAR 1:1 DAR 176:135], 28141 kb/s, 25 fps, 25 tbr, 12800 tbn, 50 tbc (default)
    Metadata:
      handler_name    : VideoHandler
      vendor_id       : [0][0][0][0]
```
我们可以调整其参数，生成更符合我们需求的视频，下面介绍下几个常见的参数。

## -r 调整帧率
不指定帧率的话，ffmpeg会使用默认的25帧，也就是1秒钟拼接25张图片，我们可以通过调整帧率的大小来控制最终生成视频的时长。
```
ffmpeg -r 10 -f image2 -i %d.jpeg output1.mp4
```
如上命令每秒会拼接10张图片，250张图片最终会生成25秒的视频。这里需要注意-r 10 参数的位置，在-i %d.jpeg前面和在后面的效果是不一样的。放在-i后面只会改变输出的视频帧率，而输入的还是默认值25，比如：
```
ffmpeg -f image2 -i %d.jpeg -r 10 output1.mp4
```
250张图片依旧只会生成10s的视频，但视频的播放征率会减小到10。

## -b:v 调整视频码率
-b:v bitrate of video。如果原始图片比较大，默认参数生成的视频大小会比较大。比如上文中我使用的图片都是2k的高清图，最终生成的10s视频就有35MB，码率有近30Mb/s（码率是指1s播过的数据量，注意这里单位是小b，bit位，大B为byte字节，1byte=8bit）。
```
ffmpeg -r 10 -f image2 -i %d.jpeg -b:v 4M output2.mp4
```
这里额外提醒下，改变码率会影响到视频清晰度，但并不意味着高码率的视频一定比低码率的视频清晰度更高，这还取决于视频编码格式，比如h265编码可以用更小的码率生成h264同等的视频质量，像av1、v8、v9等编码也优于h264。

## -vf scale 调整视频分辨率
-vf scale: Video Filter Scale
```
ffmpeg -f image2 -i %d.jpeg -s 640x480 output5.mp4
```
上面的命令会将视频直接调整为640x480的分辨率，如果原始图片不是4:3 肯定是会对原始图像做拉伸的。可以使用下面的命令等比例缩放。
```
ffmpeg -f image2 -i %d.jpeg -vf scale=-1:480 output5.mp4 
```
-1表示比例缩放，也可-vf scale=640:-1固定宽度缩放高度。以上就是几个常用的参数，这几个参数不仅限于图片转视频，视频转视频时也可以使用。