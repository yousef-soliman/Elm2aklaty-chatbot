#! /usr/local/bin/python  -*- coding: UTF-8 -*-
import json
from pprint import pprint
import random
from flask.ext.mysql import MySQL

app.config['MYSQL_DATABASE_USER'] = 'jay'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


def restaurant():
    rest = [u'كل المطاعم اهي يا عم']
    rest_str = {"allrest": rest, "do": "", "buttons": {}}
    