## gnome下设置scale factor
我们先介绍一下 GNOME 桌面缩放级别修改方式。

最简单的解决方法是打开 gnome-tweak-tool 看窗口缩放值 scale，将其调整为 1 即可。但是有时候它的值是 1 的情况下屏幕显示还是很大，将其调整为 2 没有任何改变。此时就需要使用 gsettings 命令查看 scale 值发现其实并不是 1，而是 2 。

$ gsettings get org.gnome.desktop.interface scaling-factor 
unit32 2 
这表示当前缩放级别实际是 2，使用以下命令调整为 1 即可。

$ gsettings set org.gnome.desktop.interface scaling-factor 1 