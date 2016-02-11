from base import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    salt = Column(String)


class BlockedUsers(Base):
    __tablename__ = 'blocked_users'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey(Client.id))
    block_start = Column(Date)
    block_end = Column(Date)


class LoginAttempts(Base):
    __tablename__ = 'login_attempts'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey(Client.id))
    status = Column(String)
    login_attempts = relationship(Client, backref='login_attempts')
