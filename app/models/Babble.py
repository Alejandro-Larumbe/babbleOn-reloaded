from .db import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Text

class Babble(db.Model):
  __tablename__ = 'babbles'

  id = Column(Integer, primary_key=True)
  title = Column(String(50), nullable=False)
  content = Column(Text, nullable=False)
  userID = Column(Integer, ForeignKey('users.id'), nullable=False)

  user = db.relationship('User', back_populates='babbles')
