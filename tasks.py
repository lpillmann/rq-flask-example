import time
from core import db

def slow_multiply(task_id, x, y):
    time.sleep(10)
    result = x * y
    db.engine.execute(
        'INSERT INTO results (task_id, result) ' +
        f"VALUES ('{task_id}', {result})"
    )
