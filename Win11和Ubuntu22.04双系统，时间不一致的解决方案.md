# 解决方案
1. 现在Ubuntu更新一下时间，确保时间无误：sudo apt-get install ntpdate
2. 接着输入：sudo ntpdate time.windows.com
3. 最后将时间更新到硬件上，Win7&8：sudo hwclock -w -systohc；Win10&11：sudo hwclock –localtime –systohc
