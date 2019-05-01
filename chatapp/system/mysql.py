import pymysql
from config import *


def fnSql(sql):
    db = pymysql.connect(HOST, MYSQL_NAME, MYSQL_PASSWORD, MYSQL_DATABASE)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    res = cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    db.close()
    return data


# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "123456", "python")

# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()

# # 使用 execute()  方法执行 SQL 查询
# sql = "insert into cat values(60,'水果')"
# # sql = 'select * from cat'
# # cursor.execute("INSERT INTO test.`user` (username,age) VALUES ('xiaohong',12);")
# res = cursor.execute(sql)
# print(res)
# db.commit()
# # 使用 fetchone() 方法获取单条数据.
# # data = cursor.fetchall()

# # print (data)

# # 关闭数据库连接
# db.close()
