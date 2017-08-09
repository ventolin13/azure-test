# -*- coding: utf-8 -*-
import os
import re
import datetime
from app import app
from flask import request, Blueprint


api = Blueprint('api', __name__)


@api.route('/user', methods=['POST'])
def post_user():
    pass


@api.route('/user/<string:login>', methods=['GET'])
def post_user(login):
    pass

