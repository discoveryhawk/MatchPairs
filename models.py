import datetime

from sqlalchemy import orm, create_engine, Column, Integer, BIGINT, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from config import DataBaseURI

engine = create_engine(DataBaseURI)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BIGINT)
    username = Column(String(length=255))
    fullname = Column(String(length=255))
    best_time = Column(Integer)


class Matrix(Base):
    __tablename__ = 'matrices'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    created = Column(DateTime, default=datetime.datetime.now)
    last_time_changing_time = Column(DateTime, default=datetime.datetime.now)
    matrix_items = relationship("MatrixItem", back_populates="matrix", order_by="MatrixItem.id")
    is_done = Column(Boolean, default=False)


class MatrixItem(Base):
    __tablename__ = 'matrix_items'

    id = Column(Integer, primary_key=True)
    matrix_id = Column(Integer, ForeignKey('matrices.id'))
    matrix = relationship("Matrix")
    row = Column(Integer)
    column = Column(Integer)
    value = Column(String(length=10))
    is_hidden = Column(Boolean, default=True)
    is_done = Column(Boolean, default=False)


Session = orm.sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
