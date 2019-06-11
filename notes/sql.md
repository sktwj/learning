###1. sql which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by

属于MySQL的sql_mode设置问题， 解决方法：
select @@basedir;

在 basedir + my.conf 里 加入：

```python
[mysqld]
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
```

brew services mysql restart 即可

2. 书写顺序

filter_by group_by order_by limit distinct