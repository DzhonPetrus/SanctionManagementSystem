import connector as DB

dbCur = DB.Connection.cursor()


def dbExec(sql):
    dbCur.execute(sql)
    DB.Connection.commit()


# SANCTION LOG


def newSanctionLog(StudentNo, SanctionCode, Remarks, Duration):
    sql = f"INSERT INTO SANCTIONLOG( StudentNo, SanctionCode, Remarks, Duration) VALUES('{StudentNo}', '{SanctionCode}', '{Remarks}', '{ Duration }')"
    dbExec(sql)


def updateSanctionLog(LogID, StudentNo, SanctionCode, _Status, Remarks,
                      Duration):
    sql = f"UPDATE SANCTIONLOG SET StudentNo = '{StudentNo}', SanctionCode = '{SanctionCode}',  _Status = '{_Status}', Remarks = '{Remarks}', Duration = '{Duration}' WHERE LogID = {LogID}"
    dbExec(sql)


def updateSanctionDuration(LogID, TimeServed):
    sql = f"UPDATE SANCTIONLOG SET Duration = Duration - '{TimeServed}' WHERE LogID = {LogID}"
    dbExec(sql)


def updateSanctionStatus(LogID, _Status):
    sql = f"UPDATE SANCTIONLOG SET _Status = '{_Status}' WHERE LogID = {LogID}"
    dbExec(sql)


def deleteSanctionLog(LogID):
    sql = f"DELETE FROM SANCTIONLOG WHERE LogID={LogID}"
    dbExec(sql)


def getAllSanctionLog():
    sql = f"SELECT * FROM SANCTIONLOG"
    dbCur.execute(sql)
    logs = dbCur.fetchall()
    for log in logs:
        _LogID = log[0]
        _StudentNo = log[1]
        _SanctionCode = log[2]
        _DateLog = log[3]
        _Status = log[4]
        _DateUpdated = log[5]
        _Remarks = log[6]
        _Duration = log[7]

        print(
            _LogID,
            _StudentNo,
            _SanctionCode,
            _DateLog,
            _Status,
            _DateUpdated,
            _Remarks,
            _Duration,
        )


# newSanctionLog('2018-00137-CM-0', 'sc1', 'BAD', '05:00:00')

# updateSanctionLog(1, '2018-00137-CM-0', 'sc1', 'PARTIAL', 'BAD', '03:00:00')

# deleteSanctionLog(1)

getAllSanctionLog()
