
(原文|https://webcache.googleusercontent.com/search?q=cache:Y7G_VyxvGfkJ:https://voidchen.cn/1050TI%25E7%25AC%2594%25E8%25AE%25B0%25E6%259C%25AC%25E7%259A%2584Ubuntu18%25E5%25AE%2589%25E8%25A3%2585%25E5%25AE%259E%25E8%25AE%25B0/+&cd=5&hl=zh-CN&ct=clnk&gl=id)

双显卡1050TI笔记本的Ubuntu18安装实记
置顶 | 发表于 2019-06-29 | 分类于 Linux | 阅读数 47393
前言
其实在这次安装前，我已经用了一个多星期的ubuntu-18.04.2了，在经历了数次重装和各种安装的坑之后，总算是对ubuntu有了一些理解。然后早上不知道做了个什么操作又把驱动给弄坏了，正好因为之前的安装也是一路磕磕碰碰搞错了不少东西，索性就直接再重装一次好了。吸取了之前各种驱动和软件安装的经验，想着这次应该能完美装好，所以有了这篇安装实记。一来是给自己留个记录方便以后查看（说不定又会重装= =），二来是有感于C某N上的文章抄来抄去把很多错误的、过时的办法给抄进去，让我这种小白看完跟着做一直踩坑，所以干脆把自己这次安装记录下来，我想应该也能帮助到一些同学吧。

这里我的笔记本是hp spectre x360 15，4K触摸屏（有坑）+ Nvidia GTX1050ti maxQ（巨坑），安装的是当前时间最新的一个长期支持版本ubuntu-18.04.2，这次安装包括系统安装、开发环境搭建以及系统的美化，如无意外最终的效果应该如下图所示，篇幅可能会有点长，嫌烦的同学可以根据导航栏跳转查阅。

2019-06-28 11-42-11屏幕截图

系统安装
这一部分照着官网来就好了，建议是下载LTS长期支持版，然后下面有usb烧录的教程，照着来制作USB启动盘插进去安装就好了，值得注意的主要有以下几点：

bios设置

找自己电脑型号进入bios，改成U盘启动优先，另外禁用掉安全启动，就是把secure boot设置为disable

nvidia显卡的电脑安装的时候就卡在logo界面进不去：

原因是nvidia的显卡和ubuntu自带的开源驱动Nouveau有冲突，临时解决的办法就是在开机进入grub引导界面的时候，在光标移动到Install Ubuntu这个选项的时候，按e进入到启动参数编辑界面，禁用掉显卡驱动。具体的做法就是在倒数第二行quiet slash 这句后面加一个nomodeset，空格隔开就行，然后按F10保存并启动，之后就能以低分辨率进入到安装界面。安装过车界面可能会卡卡的，鼠标动一下刷新界面显示就行，没装好驱动前只能讲究下= =

关于linux分区方案：

这边我是建议自己手动分区的，新手可以参考我这个简单分区，我是1T的固态硬盘，分区如下：

efi分区：500M，用于安装引导
/boot：500M
Swap交换分区：20G，大小最好为你实际机器内存大小的2倍
/：400G，根目录，相当于win10的C盘，后续安装的软件大多会丢里面（/opt）
/home：580G，相当于D、E、F盘，反正剩下多少都给他就好了
Nvidia驱动完美安装（巨坑）
如无意外，N卡笔记本的话安装好系统之后重启就会卡在登陆界面，输入完密码一按回车就卡住，或者登陆进去卡住，总之就是各种卡住。。。原因就是上面提到的驱动冲突问题，我们需要以禁用内置驱动的方式去登陆系统，再去安装正确的驱动。

在这里，如果之前尝试过C某D上面文章的处理办法，基本就会各种扑街= =，什么“ctrl+alt+F1进入tty模式” 啊，或者“把Nouveau驱动加入到内核禁用列表“，通通不管用。。。我甚至怀疑我们装的根本不是同一个版本（难道我的1050TI特别难装？），因为这些方法全都过时了。。参考还是可以的，比如tty模式其实ctrl+alt+F1默认就是桌面了，要进F2～F6，另外驱动没装好切过去一样是卡住的。总之，我们还是一个个问题来解决。

进入grub引导，以nomodeset模式登陆系统
首先想要进入系统，这需要和我们安装ubuntu时一样，临时把nouveau驱动给禁用掉，就是以“nomodeset”模式进入（据说ubuntu19.01的grub引导已经有专门的安全图形模式启动了）。这里首先会面临一个问题，就是装完系统重启之后，我们看不到grub引导界面就直接进入系统了。。。我去查资料发现，原来ubuntu18当电脑内只有一个系统的时候，会默认跳过grub，这需要我们进入系统后修改/etc/default/grub文件。这里又是一个死循环，想要进系统需要进入grub并修改启动参数，而想要进入grub又需要先进入系统去修改grub配置文件。。。

这显然是无解的，于是我上网找资料，看看怎么可以进入grub，然后又是在C某D上面的文章中找到 “长按shift可以进入引导界面”，显然我试过也是不行的，最后在一个别人处理矿机的帖子里找到了正确的解决办法：“在开机出现了紫色背景的时候，迅速按下ESC键” ，然后就能顺利看到grub引导界面（不行多按几下，不过按多了会进去别的），然后如同我们安装ubuntu那会一样，选中启动项，按e进入界面编辑，在倒数第二行quiet slash 这句后面加一个nomodeset，然后按F10保存并启动。

PS：之前的安装里面，我并没有看到那个”ESC进入grub“，你们知道我是怎么处理的吗，我强行分了10G硬盘出来，多装了一个ubuntu弄成双系统，就为了让他显示出grub。。。这也是为什么我能下定决心重装，因为洁癖让我很不爽这个瑕疵，虽然通过修改grub可以直接隐藏这个系统。说道这顺便贴一下这个关于grub的文章：《如何修改GRUB》，里面讲的非常细致，可以学习下。

安装最新的Nvidia 1050TI驱动
这个安装驱动也是花了我好多时间，网上找到的资料都是什么“将nouveau添加到黑名单blacklist.conf中”，又要禁用nouveau驱动，又要卸载旧的nvidia，又要加载源什么的，搞得非常复杂，又没什么len用，最后驱动没装上反倒是重装了几遍系统。实际并不需要搞这么多花里胡哨的，先联网，然后就几行代码完事了：

1
2
3
4
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
ubuntu-drivers devices
sudo ubuntu-drivers autoinstall
解释下这几句，第一句就是添加新的源，如果不添加的话，默认ubuntu版本库里最新的也就390版本，我去官网查自己的型号最新的是430版本了。第二句就是更新到本地版本库，网络不好的同学可以先更换一下国内源。第三句就是检查可以安装的驱动有哪些，看不堪都行，就是为了看看自动推荐的是不是最新的而已，都能用的。第四句就是自动安装推荐的版本了。

这里我不建议下载包自己手动装，反正我就没手动装成功过= =，如无疑外的话，重启系统应该就装好了（不需要启动的时候加nomodeset了）。打开终端，输入nvidia-smi，回车能看到以下界面就是装好了：
Screenshot

输入nvidia-settings，回车可见nvidia的设置的图形界面，这里可以切换独显和集显：


系统设置和软件安装
装好系统之后首先把日常的软件装上，先打造出日常办公环境。我也是一边装一边写这篇文章，实打实的安装配置实录啊。

更换国内源
这个网上很多，为了方便我就贴我现在用到的。
编辑apt源配置文件：sudo vi /etc/apt/sources.list
这里我还没来得及装vim，vi的操作有点不熟练，a是追加模式，找个空行把下面的阿里源复制粘贴过去就好了，里面其他的默认源最好就#注释掉。改好之后wq报存退出，并更新源sudo apt-get update

1
2
3
4
5
6
7
8
9
10
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
安装markdown编辑器Typora
为了边装边写，所以第一时间就装这个了= =，上官网找到linux版安装，也是几句代码的事,，这里我就直接贴出来了：

1
2
3
4
5
6
wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -

sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update

sudo apt-get install typora
Typora官网：https://www.typora.io/#linux

安装chrome浏览器
也是差不多的步骤，添加源，更新源，安装。唯一多了的一步就是添加了一个授权key。

1
2
3
4
sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/
sudo wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -
sudo apt-get update 
sudo apt-get install google-chrome-stable
装好就能抛弃掉自带的火狐浏览器了，卸载火狐命令如下：

1
2
dpkg --get-selections | grep firefox
sudo apt-get purge firefox firefox-locale-en firefox-locale-zh-hans
第一句就是查看装了哪些火狐相关的，第二句是指定哪些要删除，效果如图：


安装搜狗拼音输入法
搜狗输入法官网：https://pinyin.sogou.com/linux/
ubuntu18如果你在安装的时候语言选了中文，那么系统里面是内置了拼音输入法，我正是用这个输入法敲到现在，实在是不好用，所以直接安装一个搜狗输入法。我们直接去官网下载该软件，下载deb包,然后命令安装：

1
sudo dpkg -i sogoupinyin_2.2.0.0108_amd64.deb
然后就报错了= =。。。。我们还缺少一些相关依赖， sogou是基于fcitx的，而系统默认的键盘输入法系统是iBus，且ubuntu18并没有自带这个输入法，所以我们还得先安装fcitx。根据报错提示下面有一句自动修复的命令，我猜应该就是根据依赖关系自动安装一些需要的软件包吧，我们把这句命令执行一下：

1
sudo apt --fix-broken install
如无意外在软件界面就能看到fcitx小企鹅了，然后在系统设置->区域语言->管理已安装语言 那里选择输入法为fcitx，应用到系统，再重新执行一下上面安装sougo的命令，安装好后重启下系统并设置一下输入法就能用啦。
2019-06-30 17-52-00 的屏幕截图

2019-06-30 17-59-19 的屏幕截图

安装屏幕截图软件Flameshot
Flameshot这款截图软件还蛮好用的，基本满足日常需求，可以加马赛克，添加箭头和文本，安装也很简单，下面一句命令就装好了= =

1
sudo apt-get install flameshot
为了方便使用，我们还可以添加到快捷键，这个就看个人习惯了，在系统设置->设备->键盘 里设置，拉到最下面有个+号，添加一个就好了。
1561890433882

安装QQ、微信
目前试了挺多版本的QQ微信，还是deepin封装的win软件最好用，这里贴一下deepin官网：https://wiki.deepin.org/ ，感谢他们付出的努力。

先去他们提供的仓库下载deb包，如果有别的软件需要也可以上上面找找：

首先安装deepin封装好的框架：

1
2
3
git clone https://gitee.com/wszqkzqk/deepin-wine-for-ubuntu.git
cd deepin-wine-for-ubuntu
./install.sh
QQ：
http://packagess.deepin.com:8081/deepin/pool/non-free/d/deepin.com.qq.im/

1
sudo dpkg -i deepin.com.qq.im_8.9.19983deepin23_i386.deb
微信：
http://packagess.deepin.com:8081/deepin/pool/non-free/d/deepin.com.wechat/

1
sudo dpkg -i deepin.com.wechat_2.6.2.31deepin0_i386.deb
deepin官方还提供了迅雷，百度云等等各种软件，有需要的朋友可以自行找找看。我这里只用了QQ和微信，原因是有个问题一直没想到好的解决办法，就是我这个屏幕是4K屏，而deepin移植的包其实是运行在wine里，并不能随系统一起缩放，这就导致了我分辨率选4K的时候，QQ微信界面和字体都非常的小。。如果以后找到好的解决办法，我会更新到这里的QAQ

更新！！找到解决的办法啦！！
deepin的QQ和微信都是自己封装在一个wine里面，所以常规的wine设置对他来说不起作用，不过最后还是被我找到了设置deepin-wine的办法！

1
2
env WINEPREFIX="/home/chen/.deepinwine/Deepin-WeChat" deepin-wine winecfg
env WINEPREFIX="/home/chen/.deepinwine/Deepin-QQ" deepin-wine winecfg
输入这个就会弹出一个界面，上面有字体大小设置，自己去改就好啦，我把dpi改成200，如果发现改完启动秒退，可以尝试改小一点。

如果你是有别的deepin的软件，可以在~/.deepinwine/看到对应的文件夹名字，照着上面的改改就好了

安装为知笔记
官网下载：http://www.wiz.cn/download.html

一行命令安装：

1
sudo dpkg -i wiznote_2.3.2.4_amd64.deb
安装TeamViewer
官网下载：https://www.teamviewer.cn/cn/download/linux/

一行命令安装：

1
sudo dpkg -i teamviewer_14.3.4730_amd64.deb
提示依赖关系没有配置，执行以下命令修复并再次安装：

1
2
sudo apt-get -f -y install 
sudo dpkg -i teamviewer_14.3.4730_amd64.deb
安装网易云音乐
官网下载：https://music.163.com/#/download
一行命令安装：

1
sudo dpkg -i netease-cloud-music_1.2.1_amd64_ubuntu_20190428.deb
如果觉得网易云音乐UI的DPI太小，可以改下.desktop的exec：

1
Exec=netease-cloud-music --force-device-scale-factor=2 %U
安装百度网盘
官网下载：https://pan.baidu.com/download
一行命令安装：

1
sudo dpkg -i baidunetdisk_linux_2.0.1.deb
安装wps及卸载自带的Liboffice
本来我是想将就着用liboffice算了，但是用了一周发现他改完的文档格式老是有些莫名其妙的问题，所以干脆就卸载掉直接安装wps了，正好wps也有linux版。

先卸载LibOffice：

1
sudo apt-get remove libreoffice-common
安装wps：
前往官网下载deb包：https://www.wps.cn/product/wpslinux

1
sudo dpkg -i wps-office_11.1.0.8722_amd64.deb
安装配置开发环境
开发环境其实大部分都是在官网下载好，然后解压丢到/opt，配置环境变量就好了，因为每个人开发环境都不完全相同，我也不说这么细了，前往各个官网下载自己需要的版本吧。。。

Java、scala、maven安装配置
前往各个官网下载tar.gz包，sudo tar -zxvf命令，解压到/opt目录下，然后修改/etc/profile文件，添加环境变量，wq保存后自行一下 source /etc/profile 命令刷新一下就ok啦。

java官网：https://www.oracle.com/technetwork/java/javase/downloads/index.html
maven官网：http://maven.apache.org/download.cgi
scala官网：https://www.scala-lang.org/download/
1
2
3
4
5
6
export MAVEN_HOME=/opt/apache-maven-3.6.1
export JAVA_HOME=/opt/jdk1.8.0_211
export SCALA_HOME=/opt/scala-2.11.1
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:${MAVEN_HOME}/bin:${SCALA_HOME}/bin:${PATH}
1561902612761

另外还有maven的配置，设置一下本地仓库和添加国内源：

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
 <localRepository>/home/repository</localRepository>
<mirrors>
 <mirror>
          <id>alimaven</id>
          <name>aliyun maven</name>
          <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
          <mirrorOf>central</mirrorOf>
      </mirror>
      <mirror>
          <id>alimaven</id>
          <mirrorOf>central</mirrorOf>
          <name>aliyun maven</name>
          <url>http://maven.aliyun.com/nexus/content/repositories/central/</url>
      </mirror>

      <mirror>
          <id>ibiblio</id>
          <mirrorOf>central</mirrorOf>
          <name>Human Readable Name for this Mirror.</name>
          <url>http://mirrors.ibiblio.org/pub/mirrors/maven2/</url>
      </mirror>
      <mirror>
          <id>jboss-public-repository-group</id>
          <mirrorOf>central</mirrorOf>
          <name>JBoss Public Repository Group</name>
          <url>http://repository.jboss.org/nexus/content/groups/public</url>
      </mirror>

      <mirror>
          <id>central</id>
          <name>Maven Repository Switchboard</name>
          <url>http://repo1.maven.org/maven2/</url>
          <mirrorOf>central</mirrorOf>
      </mirror>
      <mirror>
          <id>repo2</id>
          <mirrorOf>central</mirrorOf>
          <name>Human Readable Name for this Mirror.</name>
          <url>http://repo2.maven.org/maven2/</url>
  </mirror>
安装idea
前往官网下载：https://www.jetbrains.com/idea/download/#section=linux

下载完解压到/opt ：

1
2
3
sudo tar -zxvf ideaIU-2019.1.3.tar.gz -C /opt
cd /opt/ideaIU-2019.1.3/bin
./idea
接下来就能看到熟悉的idea的界面啦，一直下一步配置完就好了，至于破解什么的，百度最新的方法吧hhhhhhh，安装完之后顺手先配置一下maven，免得使用默认的.m2目录又浪费时间下载（自己的本地仓库移动硬盘有备份=。=）

1561904925592

安装破解Navicat
官网下载：https://www.navicat.com/en/download/navicat-premium
下载完解压到/opt ：

1
2
3
sudo tar -zxvf navicat121_premium_cs_x64.tar.gz -C /opt
cd /opt/navicat121_premium_cs_x64/
./start_navicat
./start_navicat这句千万不要加sudo，不然等下图标就不够权限了（加了的话删除掉~/.navicat64/文件夹就行，原因是里面的配置文件是root权限的）。然后他会提示叫你安装：
1561905712468

配置好就可以启动了，就是界面非常的丑，而且不支持中文字体，会变成小方格，这些都没关系，等我们后续美化的时候，装个好看的字体，换过来就解决了= =

1561906327447

如果不想装字体的话，现在解决乱码的方式就是：先在linux系统中添加中文支持，然后手动编辑start_navicat里面的内容，将export LANG="en_US.UTF-8"将这句话改为export LANG="zh_CN.UTF-8"，然后在设置里更改字体为Noto Sans Mono CJK JP Regular，重启程序即可：

1561942237937

关于破解呢，网上有好多方法，嫌麻烦我选择删配置文件重置试用就好了，命令如下：

1
rm /home/chen/.navicat64/user.reg
另外就是这个软件的linux版本非常偷懒，图标还需要自己去创建，还需要自己下载图标。。。

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
cd /opt/navicat121_premium_cs_x64/
sudo wget http://www.navicat.com.cn/images/02.Product_00_AllProducts_Premium_large.png
sudo mv 02.Product_00_AllProducts_Premium_large.png  navicat.png

#以上为下载图标=。=，名好长顺便给改一下，然后创建图标文件：
sudo vim navicat.desktop

#在打开的文本里输入以下内容，wq保存即可
[Desktop Entry]
Encoding=UTF-8
Name=Navicat
Comment=Navicat Premium
Exec=/opt/navicat121_premium_cs_x64/start_navicat
Icon=/opt/navicat121_premium_cs_x64/navicat.png
Terminal=0
Type=Application
Categories=Application

#赋权后赋值到app目录
chmod +x navicat.desktop
sudo cp navicat.desktop /usr/share/applications/
图标路径后面主要不要有空格，执行如果出不来记得个文件夹附权，或者是sudo导致配置文件（~/.navicat64）权限为root

把用户加入到root组：sudo adduser chen root

最新更新！解决高分屏下这个navicat 缩放（UI太小，DPI低）的问题！！！
我研究了好久他的启动脚本start_navicat，发现他就是内置了一个wine，然后我们用外部的winecfg影响不到他，最后我写了个脚本。。。

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
#!/bin/sh

cd `dirname "$0"`
navicat_root=`pwd`

# Wine environment variables
WINEDIR="wine"
export LANG="en_US.UTF-8"
export PATH="$navicat_root/$WINEDIR/bin":"$navicat_root":"$navicat_root/$WINEDIR/drive_c/windows":"$PATH"
export LD_LIBRARY_PATH="$navicat_root/$WINEDIR/lib":"$navicat_root/lib":"$LD_LIBRARY_PATH"
export WINEDLLPATH="$navicat_root/$WINEDIR/lib/wine"
export WINELOADER="$navicat_root/$WINEDIR/bin/wine64"
export WINESERVER="$navicat_root/$WINEDIR/bin/wineserver"
export WINEPREFIX="$HOME/.navicat64"
export WINEDLLOVERRIDES="ucrtbase,msvcp140,vcruntime140,msvcp110,msvcr110,msxml3=n,b"

exec "${WINELOADER:-wine}" "winecfg"
把它保存为test.sh，放在跟start_navicat同级目录下面，执行一下就会弹出一个界面来，在里面改DPI就可以了！！！

安装RedisDesktopManager
官方网站：https://redisdesktop.com/download
一句命令行解决：

1
sudo snap install redis-desktop-manager
或者直接通过软件管理中心下载，如果网络卡下载不了，可以先翻墙= =

安装svn客户端
一行命令：

1
sudo apt-get install subversion
在idea中file-->settings...-->subversion--->Enable interactive mode 勾选上

1561950841243

安装git
一行命令：

1
2
3
4
sudo apt install git

git config --global user.name "VoidChen10"
git config --global user.email "425325925@qq.com"
配置ssh的config文件实现快速登录服务器
如果没装ssh的话自己装一下，我这好像是自己装了。linux的终端配置好了比xshell还方便，把服务器信息加到~/.ssh/config文件即可，没有该文件就创建一下：

1
2
3
4
5
6
7
8
9
10
11
vim .ssh/config

#配置多个服务器
Host 100    #别名
   Hostname 192.168.1.100 #服务器
   Port 22  #端口
   User root #用户
Host 172
   Hostname 172.26.152.1
   Port 2233
   User chen
编辑好wq保存下，就可以愉快的使用别名登录了，效果如下：

1561943920253

搞完之后还有个问题，就是登录还需要密码，这里我们首先生成秘钥：

1
ssh-keygen -t rsa
敲3下回车默认即可，然后把秘钥发送到服务端，由于我们刚配好了config，这里-i后面直接接别名即可：

1
ssh-copy-id -i 100
如图，已经能轻松无密码登录了~~
1561944202518

配置Hexo博客
关于如何创建和使用hexo可以参考这篇文章：《用Hexo + github搭建自己的博客 — 再也不用羡慕别人了！》
我以前弄好的直接拿过来用就好了，就是装一下npm和配置一下就好了(nodejs已经预装了)：

1
2
sudo apt install npm
npm install hexo-cli -g
把生成的公钥加到github上：1561961205561

1561961149565

测试一下github配置是否成功：

1
ssh -T git@github.com
然后hexo就装好啦，进入到博客安装目录：

1
2
3
4
hexo clean  #清理
hexo g   #打包
hexo s   #本地发布
hexo d   #上传
1561961451797

系统美化
安装gnome优化工具
1
sudo apt-get install gnome-tweak-tool
装完会多一个叫优化的程序，进去可以初步定制我们的系统了

1561945208391

安装扩展以支持安装自己的主题：

1
sudo apt-get install gnome-shell-extensions
安装完重启一下，把User themes选上：
1561946295449

添加托盘插件TopIcons
wine应用（qq、微信）不装的话启动之后会多个窗口显示托盘图标，这显然是及其难受的。。。好在有个插件可以帮我们解决，github地址：https://github.com/phocean/TopIcons-plus

1
2
3
git clone https://github.com/phocean/TopIcons-plus.git
cd TopIcons-plus
make install
这将编译glib模式并将所有必需的文件复制到您自己的用户帐户的GNOME Shell扩展目录（因此您不需要管理员权限才能运行make）。默认情况下，TopIcons Plus将存在于目录中~/.local/share/gnome-shell/extensions/TopIcons@phocean.net/。

如果要安装扩展以使其在系统范围内可用，则必须更改INSTALL_PATH变量，并以root身份运行。

1
sudo make install INSTALL_PATH=/us /share/gnome-shell/extensions
现在，重新加载GNOME Shell。您可以点击Alt+ F2，键入r，然后按Enter —或登录/注销。
重新加载Gnome

最后，启动gnome-tweak-tool实用程序来管理扩展。在那里，您可以启用TopIcons Plus，然后调整其外观。
启用TopIcons

把图片偏移设置为靠右，然后就可以看到微信在托盘里啦
1561951381360

安装Cinnamon桌面环境
首先是添加源，输入密码后，根据提示按回车继续，更新完直接安装即可

1
2
sudo add-apt-repository ppa:embrosyn/cinnamon
sudo apt update && sudo apt install cinnamon
安装好重启下，等登录那个框别急着输入密码，点那个小齿轮，选择cinnamon使用装好的桌面环境。
进去之后就是一个跟windows非常像的系统界面啦~~不过桌面还是空空如也，点击左下角的图片，找到你要用的软件，添加到桌面就好了。1561955846551

同样在这个启动菜单的左上角，就是系统设置了，里面提供了丰富的系统设置，可以根据自己的需要进行修改。

1561956014790

另外就是截图的快捷键需要重新添加了，这个自己找找吧。搜索“键盘”就能找到了。

zsh终端的使用和美化
安装zsh并让zsh作为默认的终端：

1
2
sudo apt-get install -y zsh
chsh -s /bin/zsh
装完重启下，默认的终端就是zsh了。接下来安装oh my zsh：

1
wget --no-check-certificate https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
重启终端即可看到效果，接下来修改~/.zshrc文件，加入一些好用的插件和更换主题即可。

安装高亮插件和命令自动补齐：

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
cd ~/.oh-my-zsh/custom/plugins
#高亮插件
git clone git://github.com/zsh-users/zsh-syntax-highlighting.git
#命令补齐
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

vim ~/.zshrc  #在文本内添加：
   
#设置主题，内置主题可前往github查看：https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="robbyrussell"

#添加高亮插件和自动补齐
plugins=(git zsh-syntax-highlighting zsh-autosuggestions  web-search)

#wq保存后刷新一下
source .zshrc
最后一步就是右键终端，配置首选项，把终端调整成自己喜欢的样子~~
1561964520955

安装Vimix主题
官网地址：https://www.opendesktop.org/p/1013698
直接在该页面下载下来，注意他是一个xz包，然后解压安装：

1
2
3
4
xz -d vimix-color-light.tar.xz
tar -xvf vimix-color-light.tar 
cd vimix-color-light 
sudo sh Install
安装完系统设置->主题 ，就能看到了，选一下应用即可

1561966374786

本文作者： VoidChen10
本文链接： https://voidchen.cn/1050TI笔记本的Ubuntu18安装实记/
版权声明： 本博客所有文章除特别声明外，均采用 CC BY-NC-SA 3.0 许可协议。转载请注明出处！
# 小技巧 # Linux
Spark-MLlib学习日记8：K-Means的扩展学习

文章目录
站点概览
VoidChen10
VoidChen10

11 日志
4 分类
10 标签
GitHub QQ 微博
1. 前言
2. 系统安装
3. Nvidia驱动完美安装（巨坑）
3.1. 进入grub引导，以nomodeset模式登陆系统
3.2. 安装最新的Nvidia 1050TI驱动
4. 系统设置和软件安装
4.1. 更换国内源
4.2. 安装markdown编辑器Typora
4.3. 安装chrome浏览器
4.4. 安装搜狗拼音输入法
4.5. 安装屏幕截图软件Flameshot
4.6. 安装QQ、微信
4.7. 安装为知笔记
4.8. 安装TeamViewer
4.9. 安装网易云音乐
4.10. 安装百度网盘
4.11. 安装wps及卸载自带的Liboffice
5. 安装配置开发环境
5.1. Java、scala、maven安装配置
5.2. 安装idea
5.3. 安装破解Navicat
5.4. 安装RedisDesktopManager
5.5. 安装svn客户端
5.6. 安装git
5.7. 配置ssh的config文件实现快速登录服务器
5.8. 配置Hexo博客
6. 系统美化
6.1. 安装gnome优化工具
6.2. 添加托盘插件TopIcons
6.3. 安装Cinnamon桌面环境
6.4. zsh终端的使用和美化
6.5. 安装Vimix主题
© 2019 VoidChen10
访客数 24051 总访问量 48636
0%
