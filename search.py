import pymysql
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='user',
                             password='',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print('Type ls to list all tables in db')
while True:
    table = input('\nWhich table would you like to search: ')
    if table != 'ls':
        break
    else:
        with connection.cursor() as cursor:
            cursor.execute("SHOW tables")
            x = cursor.fetchall()
            a=0
            for Xavin in x:
                print(x[a]['Tables_in_test'])
                a+=1

print('\nType ls to list fields in the table.')
while True:
    fields = input('\nFields to search: ')
    if fields != 'ls':
        break
    else:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM authors LIMIT 0")
            x = cursor.description
            a=0
            b=''
            for i in x:
                b+=x[a][0] + ', '
                a+=1
            print('\n',b)


n = input('\nHow many results would you like to fetch: ')

with connection.cursor() as cursor:

    sql = f"SELECT {fields} FROM {table}"
    cursor.execute(sql)
    result = cursor.fetchmany(int(n))
    print(result)