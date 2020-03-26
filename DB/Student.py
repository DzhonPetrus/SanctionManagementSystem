import connector as DB

dbCur = DB.Connection.cursor()


def dbExec(sql):
    dbCur.execute(sql)
    DB.Connection.commit()


# STUDENT
def newStudent(StudentNo, FName, MName, LName, XTName, ContactNo, Email, UnitNo, Street, Brgy, City, ZIP, DateOfBirth, Course, Section, SchoolYear):
    AddressID = 'A', StudentNo
    sql = f"INSERT INTO ADDRESS(AddressID, UnitNo, StreetName, Brgy, City, ZipCode) VALUES ('{AddressID}', '{UnitNo}','{Street}','{Brgy}','{City}','{ZIP}')"
    dbExec(sql)
    sql = f"INSERT INTO STUDENT(StudentNo, FName, MName, LName, XTName, ContactNo, Email, AddressID, DateOfBirth, Course, Section, SchoolYear)" \
          f"VALUES({StudentNo}, {FName}, {MName}, {LName}, {XTName}, {ContactNo}, {Email}, {AddressID}, {DateOfBirth}, {Course}, {Section}, {SchoolYear});"
    dbExec(sql)

def updateStudent(StudentNo, FName, MName, LName, XTName, ContactNo, Email, UnitNo, Street, Brgy, City, ZIP, DateOfBirth, Course, Section, SchoolYear, AddressID):
    sql = f"UPDATE ADDRESS SET UnitNo='{UnitNo}', StreetName='{Street}', Brgy='{Brgy}', City='{City}', ZipCode='{ZIP}' WHERE AddressID='{AddressID}';"
    dbExec(sql)
    sql = f"UPDATE STUDENT SET FName='{FName}', MName='{MName}', LName='{LName}', XTName='{XTName}', ContactNo='{ContactNo}', Email='{Email}', AddressID='{AddressID}', DateOfBirth='{DateOfBirth}', Course='{Course}', Section='{Section}', SchoolYear='{SchoolYear} WHERE StudentNo='{StudentNo}'';"
    dbExec(sql)

def deleteUser(StudentNo, AddressNo):
    sql = f"DELETE FROM ADDRESS WHERE AdressNo='{AddressNo}'"
    dbExec(sql)
    sql = f"DELETE FROM STUDENT WHERE StudentNo='{StudentNo}'"
    dbExec(sql)

def getAllUser():
    sql = "SELECT * FROM _USER;"
    dbCur.execute(sql)
    users = dbCur.fetchall()
    for user in users:
        print(user)
