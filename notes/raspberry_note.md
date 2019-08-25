
## 1. 信息上报

可在crontab中加入

wget -O- http://report_url/download/report.sh|bash 

定时执行 上报自己的网络和其它信息。

## 2. 串口

sudo rasp-config > Interface Actions > Serial   disable shell login +  enable harware

