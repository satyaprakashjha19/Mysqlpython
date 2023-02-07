# Fetch data
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

sql = 'Select name , roll From student'
myc = conn.cursor()
try:
    myc.execute(sql)
    row = myc.fetchone()
    while row is not None:
        print(row)
        row = myc.fetchone()
    print(myc.rowcount, "Total rows")  # rowcount

except:
    conn.rollback()    # rollback the change
    print("Unable to insert data")

myc.close()
conn.close()