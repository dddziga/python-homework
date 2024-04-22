from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    func
)
from sqlalchemy.orm import declared_attr, InstrumentedAttribute
from sqlalchemy.ext.declarative import declarative_base
from .database import db


class Base:

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    def __str__(self):
        attributes = [
            f"{name}={(getattr(self, name))!r}"
            for name, value in vars(self.__class__).items()
            if not name.startswith("_") and isinstance(value, InstrumentedAttribute)
        ]
        return f"{self.__class__.__name__}({', '.join(attributes)})"

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)
