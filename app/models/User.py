from .db import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, LargeBinary


class User(db.Model, UserMixin):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  username = Column(String(30), nullable=False, unique=True)
  first_name = Column(String(30), nullable=False)
  last_name = Column(String(30), nullable=False)
  email = Column(String(50), nullable=False, unique=True )
  hashed_password = Column(LargeBinary, nullable=False)

  babbles = db.relationship('Babble', back_populates='user' )

  @property
  def password(self):
    return self.hashed_password

  @password.setter
  def password(self, password):
    self.hashed_password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)
