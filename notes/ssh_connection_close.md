ssh connection declined

ssh_exchange_identification: Connection closed by remote host。

this issues usually due to configuration 

/etc/ssh/sshd_config

MaxSessions : max keep alive connection count

MaxStartups： max keep trying connect count 

we can ajust them to be higher, like:

MaxSessions 1000

MaxStartups 1000

sshd service sshd restart


