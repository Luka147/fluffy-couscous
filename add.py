import pymysql
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='user',
                             password='',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    sql = ''
    cursor.execute(sql)
    if 