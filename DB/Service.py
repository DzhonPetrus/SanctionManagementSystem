import connector as DB

dbCur = DB.Connection.cursor()


def dbExec(sql):
    dbCur.execute(sql)
    DB.Connection.commit()


# SANCTION LOG


def newService(LogID):
    sql = f"INSERT INTO SERVICE(LogID) VALUES('{LogID}')"
    dbExec(sql)


def updateService(ServiceID):
    sql = f"UPDATE SERVICE SET TimeOut=CURTIME() WHERE ServiceID='{ServiceID}'"
    dbExec(sql)


def deleteService(ServiceID):
    sql = f"DELETE FROM SERVICE WHERE ServiceID={ServiceID}"
    dbExec(sql)


def getAllService():
    sql = f"SELECT * FROM SERVICE"
    dbCur.execute(sql)
    services = dbCur.fetchall()
    for service in services:
        _ServiceID = service[0]
        _LogID = service[1]
        _TimeIn = service[2]
        _TimeOut = service[3]
        _ServiceDate = service[4]
        print(_ServiceID, _LogID, _TimeIn, _TimeOut, _ServiceDate)


# newService(1)

# updateService(1)

deleteService(2)

getAllService()
