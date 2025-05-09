from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.config import settings


class TaskModel(settings.DBBaseModel):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(55))
    description = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('UserModel', back_populates='tasks', lazy='joined')
