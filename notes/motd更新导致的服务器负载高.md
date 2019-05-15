
# 问题

> ssh 登录服务器经常遭遇失败, 要尝试多次才登录成功。
今天登录后top看到load奇高， 20多。
 看到大量
 /usr/bin/python3 -Es /usr/bin/lsb_release -ds进程.

# 解决过程

- ps aux |grep lsb 看到
```python
 sh -c /usr/bin/env -i PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin run-parts --lsbsysinit /etc/update-motd.d > /run/motd.dynamic.new
 调 run-parts --lsbsysinit /etc/update-motd.d 
 
 然后调 /usr/bin/python3 -Es /usr/bin/lsb_release -ds
```
- 查 /run/motd.dynamic.new 找到一篇文章 解释了。
```python

On Debian-derived systems, even with PrintMotd set to no in the sshd_config, the MOTD is still presented as part of a PAM configuration.

For instance, on my Ubuntu (and thus Debian-derived) system, in my /etc/pam.d/sshd, I see:

# Print the message of the day upon successful login.
# This includes a dynamically generated part from /run/motd.dynamic
# and a static (admin-editable) part from /etc/motd.
session    optional     pam_motd.so  motd=/run/motd.dynamic
session    optional     pam_motd.so noupdate
Commenting these out may suppress the message you are trying to eliminate.
```
- [原文链接](https://unix.stackexchange.com/questions/343248/why-am-i-still-seeing-the-motd-when-i-log-in-over-ssh)

- 因为这台服务器是由很多机器 连过来，猜测是每次建立链接服务器都会执行这个。

- 注释后 效果良好。
