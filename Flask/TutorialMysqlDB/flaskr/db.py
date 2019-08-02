import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        conn = mysql.connector.connect(host='localhost',
                                       port=3306,
                                       user='test',
                                       password='0000',
                                       db='sample',
                                       charset='utf8')
        click.echo('db connect.')
        g.db = conn
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
