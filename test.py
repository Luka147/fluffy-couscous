import pymysql
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='user',
                             password='',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

table = input('Which table would you like to search: ')

with connection.cursor() as cursor:

    sql = f"DESCRIBE {table}"
    field_search = cursor.execute(sql)


fields = ''
while True:
    fields = input('Type ls to list fields in the table.\nFields to search: ')
    if fields != 'ls':
        break
    else:
        print(field_search)

n = input('How many results would you like to fetch: ')

with connection.cursor() as cursor:

    sql = f"SELECT {fields} FROM {table}"
    cursor.execute(sql)
    result = cursor.fetchmany(int(n))
    print(result)
    