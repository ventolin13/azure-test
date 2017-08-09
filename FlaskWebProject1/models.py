# -*- coding: utf-8 -*-
# Определение архитектуры базы данных
from datetime import datetime, date
import uuid
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.mysql import TINYTEXT as Tinitext, TEXT as Text, DECIMAL as Decimal, TINYINT as Tiniint
from sqlalchemy import UniqueConstraint, Index

from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.String(64), nullable=False, unique=True, index=True)
    login = db.Column(db.String(64), nullable=False, unique=True, index=True)
    token = db.Column(db.String(12), unique=True)
    create_time = db.Column(db.DateTime)

    def __init__(self, chat_id, login):
        self.chat_id = chat_id
        self.login = login
        self.create_time = datetime.utcnow().replace(microsecond=0)
        self.token = str(uuid.uuid4())[-12:]
