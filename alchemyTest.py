from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

Base = declarative_base()

DB_session = sessionmaker(bind=engine)

session = DB_session()


class User(Base):
    __tablename__ = 'User'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    lineid = Column('lineid', String(256))
    name = Column('name', String(10))
    email = Column('email', String(30))
    facebook = Column('facebook', String(50))
    intro = Column('intro', String(100))



def addUser(addLineid, addName, addEmail, addFacebook, addIntro):
    session = DB_session()
    aUser = User(lineid=addLineid, name=addName, email=addEmail,
                 facebook=addFacebook, intro=addIntro)
    session.add(aUser)
    session.commit()
    session.close()
    print(aUser.id)



def checkRepeat(searchLineid):
    session = DB_session()
    check = session.query(User).filter(User.lineid == searchLineid).count()
    session.close()
    if(check > 1):
        return True
    else:
        return False


def searchUserID(searchLineid):
    session = DB_session()
    sUser = session.query(User).filter(User.lineid == searchLineid).first()
    session.close()
    return sUser.lineid


def searchUserName(searchLineid):
    session = DB_session()
    sUser = session.query(User).filter(User.lineid == searchLineid).first()
    session.close()
    return sUser.name


session.close()

# Test code

# Base.metadata.create_all(engine)
# u = User(lineid="lol", name="豪哥", email="toooair@gmail.com", facebook="facebook.com/toooair", intro="你是在哈囉？")
# session.add(u)
# session.commit()
# print(u.id)

# nid = session.query(User).filter(User.lineid == "lol").count()
# print(nid)