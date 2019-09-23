
## 记录

1ORDER BY 多列

```sql

mysql> select * from websites order by country,alexa;
+----+----------+-------------------+-------+---------+
| id | name     | url               | alexa | country |
+----+----------+-------------------+-------+---------+
|  4 | 微博     | weibo.com         |    20 | CN      |
|  2 | 学习     | taobao.com        |   333 | CN      |
|  3 | 菜鸟     | runboob.com       |  4000 | CN      |
|  5 | facebook | facebook.com      |     3 | US      |
|  1 | google   | http://google.com |   232 | US      |
+----+----------+-------------------+-------+---------+
5 rows in set (0.04 sec)
```
2 INSERT INTO 2种方法


```sql
INSERT INTO table_name
VALUES (value1,value2,value3,...);

INSERT INTO table_name (column1,column2,column3,...)
VALUES (value1,value2,value3,...);

```
3 sql_safe_updates 

执行没有 WHERE 子句的 UPDATE 要慎重，再慎重。

在 MySQL 中可以通过设置 sql_safe_updates 这个自带的参数来解决，当该参数开启的情况下，你必须在update 语句后携带 where 条件，否则就会报错。

set sql_safe_updates=1; 表示开启该参数

4 SQL 通配符

``` 
%     0或多个

_     替代一个字符
[charlist]   字符列中的任何单一字符
[^charlist]   不在字符列中的任何单一字符

下面的 SQL 语句选取 name 以 "G"、"F" 或 "s" 开始的所有网站：

SELECT * FROM Websites WHERE name REGEXP '^[GFs]';

下面的 SQL 语句选取 name 不以 A 到 H 字母开头的网站：

SELECT * FROM Websites WHERE name REGEXP '^[^A-H]';

```

5 concat 连接字段

在下面的 SQL 语句中，我们把三个列（url、alexa 和 country）结合在一起，并创建一个名为 "site_info" 的别名：
```sql


mysql> select name, concat(url, ',', alexa) as site_info from websites;
+----------+--------------------------+
| name     | site_info                |
+----------+--------------------------+
| google   | http://google.com,232    |
| 学习     | taobao.com,333           |
| 菜鸟     | runboob.com,4000         |
| 微博     | weibo.com,20             |
| facebook | facebook.com,3           |
| hehe     | hehe.com,21              |
| 百度     | https://www.baidu.com/,4 |
+----------+--------------------------+
7 rows in set (0.05 sec)
```

6  表别名

```sql

mysql> select w.name, w.url, a.count, a.date from websites as w, access_log as a where a.site_id=w.id and w.name="菜鸟";
+------+-------------+-------+---------------------+
| name | url         | count | date                |
+------+-------------+-------+---------------------+
| 菜鸟 | runboob.com |  1111 | 2019-09-01 22:50:02 |
+------+-------------+-------+---------------------+
1 row in set (0.02 sec)
```

在下面的情况下，使用别名很有用：
```text
在查询中涉及超过一个表
在查询中使用了函数
列名称很长或者可读性差
需要把两个列或者多个列结合在一起
```

7 