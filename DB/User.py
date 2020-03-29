import connector as DB

dbCur = DB.Connection.cursor()


def dbExec(sql):
    dbCur.execute(sql)
    DB.Connection.commit()


# _USER


def newUser(username, password, role):
    sql = f"INSERT INTO _USER(_Username, _Password, _Role) VALUES ('{username}','{password}',{role});"
    dbExec(sql)


def updateUser(userID, username, password, role):
    sql = f"UPDATE _USER SET _Username='{username}', _Password='{password}', _Role={role} WHERE UserID={userID};"
    dbExec(sql)


def deleteUser(userID):
    sql = f"DELETE FROM _USER WHERE UserID={userID}"
    dbExec(sql)


def getAllUser():
    sql = "SELECT * FROM _USER;"
    dbCur.execute(sql)
    users = dbCur.fetchall()
    for user in users:
        _userID = user[0]
        _username = user[1]
        _password = user[2]
        _role = user[3]

        print(_userID, _username, _password, _role)

def checkExistingUser(username,password):
    sql = f"SELECT * FROM _USER WHERE _Username='{username}' AND _Password='{password}'"
    dbCur.execute(sql)
    row = dbCur.fetchone()
    if row == None:
        return False
    else:
        return row


# newUser('ADMIN', 'ADMIN', 1)

# newUser('STAFF', 'STAFF', 0)

# updateUser(2, 'STAFF2', 'STAFF', 0)

getAllUser()

