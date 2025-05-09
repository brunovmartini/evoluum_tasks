from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from core.config import settings


class UserModel(settings.DBBaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), index=True, nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    tasks = relationship(
        'TaskModel',
        cascade='all,delete-orphan',
        back_populates='creator',
        uselist=True,
        lazy='joined'
    )
