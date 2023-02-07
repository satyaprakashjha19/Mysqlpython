# Creating Connection
# Type 1
"""import mysql.connector
try:
    conn = mysql.connector.connect(user='root',
                               password='Sonu9RT@#576',
                               host='localhost',
                               port='3306')
except:
    print("Unable to Connect")"""

# Type 2
import mysql.connector

config = {
    'user': 'root',
    'password': 'Sonu9RT@#576',
    'host': 'localhost',
    'port': '3306'
}

try:
    conn = mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("connected")
except:
    print("Unable to connect")

myc = conn.cursor()
myc.execute('SHOW DATABASES')
for i in myc:
    print(i)

myc.close()
conn.close()
