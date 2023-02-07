# Connecting to database

import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='Sonu9RT@#576',
        host='localhost',
        database='pythondb',
        port='3306'
    )
    if(conn.is_connected()):
        print("connected")

except:
    print("Unable to connect")

# Create table

sql = "CREATE TABLE Teacher(teacherid INT AUTO_INCREMENT PRIMARY KEY,name varchar(20), age int, salary FLOAT)"
myc = conn.cursor()
myc.execute(sql)
myc.close()
conn.close()

