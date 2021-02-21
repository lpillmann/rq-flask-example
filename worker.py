from rq import Connection, Worker
from core import app, queue

with app.app_context():
    with Connection():
        w = Worker([queue])
        w.work()
