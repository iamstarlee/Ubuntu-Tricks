After installing cuda 11.8 and cudnn 8.6, I got the error below when I use 'sudo apt-get autoremove'
```bash
/sbin/ldconfig.real: /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 is not a symbolic link

/sbin/ldconfig.real: /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8 is not a symbolic link

/sbin/ldconfig.real: /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_ops_train.so.8 is not a symbolic link

/sbin/ldconfig.real: /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 is not a symbolic link

/sbin/ldconfig.real: /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8 is not a symbolic link

/sbin/ldconfig.real: /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8 is not a symbolic link

/sbin/ldconfig.real: /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn.so.8 is not a symbolic link

```

you need to recreate the symbolic link, use the commands below:
```bash
cd /usr/local/cuda-11.8/lib64

sudo ln -sf libcudnn.so.8.6.0 libcudnn.so.8
sudo ln -sf libcudnn.so.8 libcudnn.so

sudo ln -sf libcudnn.so.8.6.0 libcudnn_ops_infer.so.8
sudo ln -sf libcudnn_ops_infer.so.8 libcudnn.so

sudo ln -sf libcudnn.so.8.6.0 libcudnn_ops_train.so.8
sudo ln -sf libcudnn_ops_train.so.8 libcudnn.so

sudo ln -sf libcudnn.so.8.6.0 libcudnn_adv_train.so.8
sudo ln -sf libcudnn_adv_train.so.8 libcudnn.so

sudo ln -sf libcudnn.so.8.6.0 libcudnn_adv_infer.so.8
sudo ln -sf libcudnn_adv_infer.so.8 libcudnn.so

sudo ln -sf libcudnn.so.8.6.0 libcudnn_cnn_infer.so.8
sudo ln -sf libcudnn_cnn_infer.so.8 libcudnn.so

```
Change the command to match your cuda, cudnn version.
