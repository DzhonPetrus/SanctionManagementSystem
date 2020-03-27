import connector as DB

dbCur = DB.Connection.cursor()


def dbExec(sql):
    dbCur.execute(sql)
    DB.Connection.commit()


# SANCTION


def newSanction(SanctionCode, TypeID, _Description):
    sql = f"INSERT INTO SANCTION(SanctionCode, TypeID, _Description) VALUES ('{SanctionCode}', '{TypeID}', '{_Description}')"
    dbExec(sql)


def updateSanction(SanctionCode, TypeID, _Description):
    sql = f"UPDATE SANCTION SET TypeID='{TypeID}', _Description='{_Description}' WHERE SanctionCode='{SanctionCode}'"
    dbExec(sql)


def deleteSanction(SanctionCode):
    sql = f"DELETE FROM SANCTION WHERE SanctionCode='{SanctionCode}'"
    dbExec(sql)


def getAllSanctions():
    sql = "SELECT * FROM SANCTION"
    dbCur.execute(sql)
    sanctions = dbCur.fetchall()
    for sanction in sanctions:
        _SanctionCode = sanction[0]
        _TypeID = sanction[1]
        _Description = sanction[2]
        print(_SanctionCode, _TypeID, _Description)


# newSanction('sc1', 'A-101', 'BRUH')
# newSanction('sc2', 'A-101', 'BRUH')
# updateSanction('sc1', 'A-101', 'NEW DESCRIPTION')
# deleteSanction('sc2')
# getAllSanctions()
