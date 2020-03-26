from mysql.connector import connect
import sys

#SETUP THE CONNECTION
try:
    dbCon = connect(
        host='localhost',
        database='SANCTION_MANAGEMENT',
        user='root',
        password='root'
    )
    dbCur = dbCon.cursor()
except:
    print("Cannot connect to the database.")