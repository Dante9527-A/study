import pymysql

args = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"dict",
    "charset":"utf8"
}

db = pymysql.connect(**args)

cur = db.cursor()

sql = "select mean from words where word = %s;"
cur.execute(sql,[input("请输入需要查询的单词：")])

one = cur.fetchone()
print(one)

cur.close()
db.close()