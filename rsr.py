# Retrieve single row
# with where clause parameter query tuple

import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root',
        password='Sonu9RT@#576',
        host='localhost',
        database='pythondb',
        port='3306'
    )
    if (conn.is_connected()):
        print("connected")
except:
    print("Unable to connect")

sql = 'Select * From student Where stuid=%s'
myc = conn.cursor()
disp_value = (11,)
try:
    myc.execute(sql, disp_value)
    row = myc.fetchone()
    print(row)
    print("Total Rows: ", myc.rowcount)
except:
    print("Unable to retrieve data")

myc.close()  # close cursor
conn.close() # close connection