import connector as DB

dbCur = DB.Connection.cursor()


def dbExec(sql):
    dbCur.execute(sql)
    DB.Connection.commit()


# STUDENT


def newAddress(AddressID, UnitNo, Street, Brgy, City, ZIP):
    sql = f"INSERT INTO ADDRESS(AddressID, UnitNo, StreetName, Brgy, City, ZipCode) VALUES('{AddressID}','{UnitNo}','{Street}','{Brgy}','{City}','{ZIP}')"
    dbExec(sql)


def updateAddress(AddressID, UnitNo, Street, Brgy, City, ZIP):
    sql = f"UPDATE ADDRESS SET UnitNo='{UnitNo}', StreetName='{Street}', Brgy='{Brgy}', City='{City}', ZipCode='{ZIP}' WHERE AddressID='{AddressID}';"
    dbExec(sql)


def deleteAddress(AddressID):
    sql = f"DELETE FROM ADDRESS WHERE AddressID='{AddressID}'"
    dbExec(sql)


def getAddress(AddressID):
    sql = f"SELECT * FROM ADDRESS WHERE AddressID='{ AddressID }';"
    dbCur.execute(sql)
    users = dbCur.fetchall()
    for user in users:
        _AddressID = user[0]
        _UnitNo = user[1]
        _StreetNo = user[2]
        _Brgy = user[3]
        _City = user[4]
        _ZipCode = user[5]
    print(_AddressID, _UnitNo, _StreetNo, _Brgy, _City, _ZipCode)


# newAddress('A-2018-00137-CM-0', '1', '1', '1', '1', '1')
# updateAddress('A-101', '2', '2', '2', '2', '2')
# getAddress('A-101')
# deleteAddress('A-101')
