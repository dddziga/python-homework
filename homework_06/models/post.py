from sqlalchemy import (
    Column,
    String,
    Text,
)

from .base import Base
from .database import db


class Post(db.Model, Base):
    def __init__(self, user_id, title, body):
        self.user_id = user_id
        self.title = title
        self.body = body

    def __repr__(self):
        return "<Post('%s','%s', '%s')>" % (self.user_id, self.title, self.body)

    title = Column(String)
    body = Column(Text)
