from alchemyStart import DB_session
from alchemyModel import User


def addUser(addLineid, addName, addEmail, addFacebook, addIntro):
    session = DB_session()
    aUser = User(lineid=addLineid, name=addName, email=addEmail,
                 facebook=addFacebook, intro=addIntro)
    session.add(aUser)
    session.commit()
    session.close()


# Search By LineID
def checkRepeat(searchLineid):
    session = DB_session()
    check = session.query(User).filter(User.lineid == searchLineid).count()
    session.close()
    if(check >= 1):
        return True
    else:
        return False


def searchUserID(searchLineid):
    session = DB_session()
    sUser = session.query(User).filter(User.lineid == searchLineid).first()
    session.close()
    return sUser.id


def searchUserName(searchLineid):
    session = DB_session()
    sUser = session.query(User).filter(User.lineid == searchLineid).first()
    session.close()
    return sUser.name

# Search by ID


def searchUser(searchID):
    session = DB_session()
    sUser = session.query(User).filter(User.id == searchID).first()
    session.close()
    return sUser
