
装了个navicat，可要自己做desktop文件, 图标是放在/usr/share/pixmaps/下
Icon里只写图标文件名就可以，不要写扩展名也不要有空格　

Caution:
icon file should be under /usr/share/pixmaps folder
desktop file should be under /usr/share/applications folder



desktop file format like below:
Icon value only should be one words, strip space and comment.

```
[Desktop Entry]
Encoding=UTF-8
Name=navicat
Comment=The Smarter Way to manage dadabase
Exec=/home/t/tools/navicat120_premium_cs_x64/start_navicat
Icon=navicat
Categories=Application;Database;MySQL;navicat
Version=1.0
Type=Application
Terminal=0

```




