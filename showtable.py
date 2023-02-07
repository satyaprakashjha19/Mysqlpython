# Show the tables in the database

import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='Sonu9RT@#576',
        host='localhost',
        database='pythonDB',
        port='3306'
    )
    if(conn.is_connected()):
        print("connected")

except:
    print("Unable to connect")

sql = "Show tables"
myc = conn.cursor()
myc.execute(sql)
for i in myc:
    print(i)
myc.close()
conn.close()