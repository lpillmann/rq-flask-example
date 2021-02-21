from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from rq import Queue
from redis import Redis

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://localhost:5432/postgres'
db = SQLAlchemy(app)
queue = Queue(connection=Redis())
