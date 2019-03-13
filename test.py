import pymysql
import pymysql.cursors
import json

connection = pymysql.connect(host='localhost',
                             user='user',
                             password='',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

table = input('Which table would you like to search: ')

fields = ''
while True:
    fields = input('Type ls to list fields in the table.\nFields to search: ')
    if fields != 'ls':
        break
    else:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM authors LIMIT 0")
            x = cursor.description
            a=0
            for i in x:
                print(x[a][0])
                a+=1

n = input('How many results would you like to fetch: ')

with connection.cursor() as cursor:

    sql = f"SELECT {fields} FROM {table}"
    cursor.execute(sql)
    result = cursor.fetchmany(int(n))
    print(result)
    