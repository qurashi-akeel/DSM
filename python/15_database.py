import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mySql@123"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE IF NOT EXISTS test.test123 (c1 INT)")

# mycursor.execute(
#     "INSERT INTO test.test_table VALUES(100, 'testuser123', 12345)"
#     )

mycursor.execute("SELECT sno FROM test.test_table")
for item in mycursor.fetchall():
    print(item[0])


mydb.commit()
mydb.close()
