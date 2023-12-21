
## 交互式进入一个容器
docker run -it --rm ubuntu:18.04 bash

## 要想列出已经下载下来的镜像，可以使用 docker image ls 命令。

## 你可以通过 docker system df 命令来便捷的查看镜像、容器、数据卷所占用的空间。

##而出现仓库名、标签均为 <none> 的镜像。这类无标签镜像也被称为 虚悬镜像(dangling image) ，可以用下面的命令专门显示这类镜像：
$ docker image ls -f dangling=true

## docker image prune

