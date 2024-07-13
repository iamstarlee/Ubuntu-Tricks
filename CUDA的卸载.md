## 卸载用run方式安装的CUDA
```bash
# cuda10.0及以下的卸载
cd /usr/local/cuda-xx.x/bin/
sudo ./uninstall_cuda_xx.x.pl
sudo rm -rf /usr/local/cuda-xx.x

# cuda10.1及以上的卸载
cd /usr/local/cuda-xx.x/bin/
sudo ./cuda-uninstaller
sudo rm -rf /usr/local/cuda-xx.x

```
