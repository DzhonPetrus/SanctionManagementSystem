from mysql.connector import connect

#SETUP THE CONNECTION
try:
    Connection = connect(
        host='localhost',
        database='SANCTION_MANAGEMENT',
        user='root',
        password='root'
    )
except:
    print("Cannot connect to the database.")
