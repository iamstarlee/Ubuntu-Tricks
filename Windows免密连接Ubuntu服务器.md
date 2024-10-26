要实现SSH免密登录，首先需要准备一组公钥和私钥。将公钥放到服务器上，将私钥放到客户机上。当客户机连接服务器时，服务器会根据自身的公钥校验客户机的私钥，如果校验通过则允许连接。

![image](https://github.com/user-attachments/assets/57478653-71d6-4f20-8d20-d034c8ff570f)

## 在Windows上生成公钥和私钥
1. 进入到C:\Users\dell\.ssh
2. 右键打开Git Bash Here
3. 输入ssh-keygen -t rsa
4. 直接enter enter enter
![image](https://github.com/user-attachments/assets/25d7c83a-9b0c-46e4-82a5-9922c5d961ff)
5. 此时C:\Users\dell\.ssh目录下会生成一个id_rsa文件和一个id_rsa.pub文件

## 上传公钥到Ubuntu并测试免密登录
1. 进入到C:\Users\dell\.ssh
2. ssh-copy-id Ubuntu的用户名@Ubuntu的IP地址
3. ssh Ubuntu的用户名@Ubuntu的IP地址
