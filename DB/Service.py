import connector as DB
import SanctionLog
import datetime

dbCur = DB.Connection.cursor()


def dbExec(sql):
    dbCur.execute(sql)
    DB.Connection.commit()


# SANCTION LOG


def newService(LogID):
    sql = f"INSERT INTO SERVICE(LogID) VALUES('{LogID}')"
    dbExec(sql)


def updateService(ServiceID, LogID):
    sql = f"UPDATE SERVICE SET TimeOut=CURTIME() WHERE ServiceID='{ServiceID}'"
    dbExec(sql)
    _TimeIn = getServiceTimeIn(ServiceID)
    _TimeOut = datetime.datetime.now().time()
    print("TIME OUT", _TimeOut, "TIME IN", _TimeIn)
    TimeServed = (_TimeOut - _TimeIn)
    SanctionLog.updateSanctionDuration(LogID, TimeServed)


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

        if _TimeOut is not None:
            TimeServed = _TimeOut - _TimeIn
            print(_ServiceID, _LogID, _TimeIn, _TimeOut, _ServiceDate,
                  TimeServed)
        else:
            print(_ServiceID, _LogID, _TimeIn, _TimeOut, _ServiceDate)


def getServiceTimeIn(ServiceID):
    sql = f"SELECT TimeIn FROM SERVICE WHERE ServiceID={ServiceID}"
    dbCur.execute(sql)
    records = dbCur.fetchall()
    for record in records:
        return record[0]


# newService(1)

updateService(1, 4)

# deleteService(2)
getAllService()
