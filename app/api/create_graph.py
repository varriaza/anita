import string
import sys
from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import *


@api.route('/<ip_db>/<table>/table_data/all')
def get_table_data(ip_db, table):
    try:
        engine_ip_db = ip_db.replace('query','session')
        table_uppercase = string.capwords(table)
        table_class = reduce(getattr, table_uppercase.split("."), sys.modules[__name__])
        engine = getattr(table_class,engine_ip_db)
        locations = engine.execute("select column_name from information_schema.columns where table_name = '" + table + "'").fetchall()
        return jsonify({'table_data': [item[0] for item in locations]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})

@api.route('/<ip_db>/table_names')
def get_tables(ip_db):
    try:
        engine_ip_db = ip_db.replace('query','session')
        engine = getattr(Adu5_pat,engine_ip_db)
        test = engine.execute("select table_name from information_schema.tables").fetchall()
        print test
        return jsonify({'tables': [item[0] for item in test]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})









