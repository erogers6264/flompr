# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
	 abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = '/tmp/flompr.db'
DEBUG = True
SECRET_KEY = '39522958611'
USERNAME = 'ethan'
PASSWORD = '1'

# create our little cute tiny app :)
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db:
	with closing(connect_db()) as db:
		with app.open_resource('flompr.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

if __name__ == '__main__':
	app.run()