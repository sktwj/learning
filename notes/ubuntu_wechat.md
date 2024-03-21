

## 1 优麒麟
### 1.1 更改系统配置 
>sudo cp /etc/lsb-release /etc/lsb-release.bck
sudo tee /etc/lsb-release << EOF
DISTRIB_ID=Kylin
DISTRIB_RELEASE=V10
DISTRIB_CODENAME=kylin
DISTRIB_DESCRIPTION="Kylin V10 SP1"
DISTRIB_KYLIN_RELEASE=V10
DISTRIB_VERSION_TYPE=enterprise
DISTRIB_VERSION_MODE=normal
EOF
### 1.2 安装优麒麟微信
[优麒麟](https://www.ubuntukylin.com/applications/106-cn.html)
安装后登录一次，然后卸载掉。

### 1.3 安装民间微信
微信名字是 [wechat-beta_1.0.0.145_amd64.deb](https://www.123pan.com/s/MEdbVv-r0vY3.html)



## 2. docker微信
 [手把手](https://blog.csdn.net/qq_43827595/article/details/109487664)

2种方式都比较稳定。 