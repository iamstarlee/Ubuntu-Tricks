查看环境
```
conda info --envs
```

导出环境
```
conda env export > py36.yaml
```

会生成一个py36.yaml文件，将其复制到目标机上后执行导入环境操作：
```
conda env create -f py36.yaml
```

注意：若导出base环境，则在目标机上会提示已存在（而且base环境无法删除）。所以要想导出base，最好先复制一下，再导出复制品：
```
conda create -n new_name --clone base
```

再导出new_name环境即可。必要的话再在原机删除复制环境：
```
conda remove -n new_name --all
```

在用的时候发现有些module还是未安装，上网找了下原因，原来以上只会导出conda命令直接安装的包，而我的包大多是用pip安装在Anaconda的lib和site-package里了。因此还要用导出pip的方法：
pip导出安装的库到27.txt：
```
pip freeze > 27.txt
```

pip导入27.txt中列出的库到新机：
```
pip install -r 27.txt
```
