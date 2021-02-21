import uuid

from flask import request, jsonify, abort
from rq import Connection, Worker

from core import app, db, queue
from tasks import slow_multiply


@app.route('/multiply', methods=['POST'])
def submit_multiplication():
    """Queue a multiplication and return the task ID."""
    body = request.get_json(force=True)
    task_id = uuid.uuid4()  # new unique id
    queue.enqueue(
        slow_multiply,
        task_id, body['x'], body['y']
    )
    return jsonify({'task_id': str(task_id)}), 202

@app.route('/multiply/<task_id>', methods=['GET'])
def get_multiplication(task_id):
    """Return the result for a task ID, if completed."""
    query_result = db.engine.execute(
        f"SELECT result FROM results WHERE task_id = '{task_id}'"
    ).first()
    if query_result is None:
        abort(404)
    else:
        return jsonify({'result': str(query_result[0])})

if __name__ == '__main__':
    app.run()
