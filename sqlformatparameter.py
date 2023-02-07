# Mysql parameterized query
# tuple and dictionary
# executemany method

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

sql = "INSERT INTO student(name, roll, fees) VALUES (%s, %s, %s)"

myc = conn.cursor()

seq_params = [("jai", 111, 80000.23), ("Santosh", 112, 65000.56)]
try:
    myc.executemany(sql, seq_params)
    conn.commit()                         # Committing the change

except:
    conn.rollback()    # rollback the change
    print("Unable to insert data")

myc.close()
conn.close()