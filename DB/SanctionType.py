import connector as DB

dbCur = DB.Connection.cursor()


def dbExec(sql):
    dbCur.execute(sql)
    DB.Connection.commit()


# SANCTION TYPE


def newSanctionType(TypeID, _Description):
    sql = f"INSERT INTO SANCTIONTYPE(TypeID, _Description) VALUES('{TypeID}','{_Description}')"
    dbExec(sql)


def updateSanctionType(TypeID, _Description):
    sql = f"UPDATE SANCTIONTYPE SET _Description='{_Description}' WHERE TypeID='{TypeID}'"
    dbExec(sql)


def deleteSanctionType(TypeID):
    sql = f"DELETE FROM SANCTIONTYPE WHERE TypeID='{TypeID}'"
    dbExec(sql)


def getAllSanctionType():
    sql = f"SELECT * FROM SANCTIONTYPE"
    dbCur.execute(sql)
    types = dbCur.fetchall()
    for _type in types:
        _TypeID = _type[0]
        _Description = _type[1]
        print(_TypeID, _Description)


# newSanctionType('A-101', 'NEW TYPE')

# newSanctionType('CXZ1', 'ZXCNASDNA')

# updateSanctionType('A1', 'NEW DESCRIPTION')

# getAllSanctionType()

# deleteSanctionType('A1')

getAllSanctionType()
