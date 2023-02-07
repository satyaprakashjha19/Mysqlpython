# Create single and multiple  row

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

sql = "INSERT INTO student(name, roll, fees) VALUES ('Spider', 108, 90000.52)," \
      "('Ramona', 109, 600012.52), ('pratt', 110, 444000.52)"
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()                         # Committing the change
    print(myc.rowcount , "Rows inserted")  # rowcount
    print(myc.lastrowid)            # last row id
except:
    conn.rollback()    # rollback the change
    print("Unable to insert data")

myc.close()
conn.close()