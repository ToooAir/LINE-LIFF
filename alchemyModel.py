from alchemyStart import Base

from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'User'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    lineid = Column('lineid', String(256))
    name = Column('name', String(10))
    email = Column('email', String(30))
    facebook = Column('facebook', String(50))
    intro = Column('intro', String(100))
