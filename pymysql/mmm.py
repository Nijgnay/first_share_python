import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="Aaaxyjnb666!",
    database="db1",
    charset="utf8mb4"  # 必须加，注意是utf8，不是utf-8
)

#创建游标执行sql
cursor = conn.cursor()
#执行查询语句
sql =""
cursor.execute(sql)

conn.commit()#提交
#关闭资源
cursor.close()
conn.close()