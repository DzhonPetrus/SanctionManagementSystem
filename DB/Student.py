import connector as DB

dbCur = DB.Connection.cursor()


def dbExec(sql):
    dbCur.execute(sql)
    DB.Connection.commit()


# STUDENT


def newStudent(StudentNo, FName, MName, LName, XTName, ContactNo, Email,
               DateOfBirth, Course, Section, SchoolYear):
    AddressID = "A-" + StudentNo[:10]
    sql = f"INSERT INTO ADDRESS(AddressID) VALUES('{ AddressID }');"
    dbExec(sql)
    sql = f"INSERT INTO STUDENT(StudentNo, FName, MName, LName, XTName, ContactNo, Email, AddressID, DateOfBirth, Course, Section, SchoolYear) VALUES('{StudentNo}', '{FName}', '{MName}', '{LName}', '{XTName}', {ContactNo}, '{Email}', '{AddressID}', '{DateOfBirth}', '{Course}', '{Section}', {SchoolYear});"
    dbExec(sql)


def updateStudent(StudentNo, FName, MName, LName, XTName, ContactNo, Email,
                  DateOfBirth, Course, Section, SchoolYear):
    sql = f"UPDATE STUDENT SET FName='{FName}', MName='{MName}', LName='{LName}', XTName='{XTName}', ContactNo='{ContactNo}', Email='{Email}', DateOfBirth='{DateOfBirth}', Course='{Course}', Section='{Section}', SchoolYear={SchoolYear} WHERE StudentNo='{StudentNo}';"
    dbExec(sql)


def deleteUser(StudentNo, AddressNo):
    sql = f"DELETE FROM ADDRESS WHERE AdressNo='{AddressNo}'"
    dbExec(sql)
    sql = f"DELETE FROM STUDENT WHERE StudentNo='{StudentNo}'"
    dbExec(sql)


def getStudentByNo(StudentNo):
    sql = f"SELECT * FROM STUDENT WHERE StudentNo='{StudentNo}';"
    dbCur.execute(sql)
    return dbCur.fetchone()


def getAllStudent():
    sql = "SELECT * FROM STUDENT;"
    dbCur.execute(sql)
    return dbCur.fetchall()
    # for student in students:
    #     _StudentNo = student[0]
    #     _FName = student[1]
    #     _MName = student[2]
    #     _LName = student[3]
    #     _XTName = student[4]
    #     _ContactNo = student[5]
    #     _Email = student[6]
    #     _DateOfBirth = student[7]
    #     _Course = student[8]
    #     _Section = student[9]
    #     _SchoolYear = student[10]

    # print(_StudentNo, _FName, _MName, _LName, _XTName, _ContactNo, _Email,
    #       _DateOfBirth, _Course, _Section, _SchoolYear)


# newStudent('2018-00137-CM-0', 'Juan', 'Dalisay', 'Pedro', 'Sr', '09196429771',
#            'juanpedro@gmail.com', '1999-11-19', 'BSIT', '1', 2018)

# updateStudent('2018-00137-CM-0', 'Juan', 'Dalisay', 'Pedro', 'Sr',
#               '09196429771', 'newjuanpedro@gmail.com', '1999-11-19', 'BSHRDM',
#               '1', 2018)

# deleteUser('2018-00137-CM-0', 'A-2018-00137-CM-0')

# getAllStudent()
