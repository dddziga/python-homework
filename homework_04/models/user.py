"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""


from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    ForeignKey
)
from sqlalchemy .orm import relationship, sessionmaker
from .base import Base


class User(Base):
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.username, self.email)

    name = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)

    posts = relationship("Post", back_populates="user")

