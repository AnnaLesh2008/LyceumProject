import datetime
import sqlalchemy
from flask import session
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase, SerializerMixin, UserMixin):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)

    user = orm.relationship('User')
