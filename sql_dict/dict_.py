"""
创建连接调用数据
"""
import pymysql

import re

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='dict',
                     charset='utf8')
# 获取游标(用于进行数据操作的对象，承载操作结果)
cur = db.cursor()

dict_ = open('dict.txt')
sql = "insert into words(word,mean)\
        values (%s,%s);"

for line in dict_:  # 文本文件可用for来迭代 按行读取
    tup = re.findall(r'(\S+)\s+(.*)', line)[0]
    print(tup)
    try:
        cur.execute(sql, tup)
        # 允许连续执行多个sql语句 一同提交
    except Exception as e:
        db.rollback()  # 退回到commit
db.commit()
# 关闭数据库
cur.close()
db.close()
