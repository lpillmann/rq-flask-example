# rq-flask-example

This is an example of how to use `rq` to manage long running jobs submitted via a Flask API.

Code is mostly from [acroz's website](https://acroz.dev/2018/01/07/data-science-apis-long-running-tasks/), adapted to fix bugs existing in original version.

# How to use

## Dependencies

- Redis (install and leave it running in background)
- Postgres (install and leave a localhost running in background - use default with no user, no password)
- Install Python modules using Poetry (`poetry install`)

## Run

### Server side

Activate env
```bash
poetry shell
```

Run Flask app
```bash
python views.py
```

Start rq worker
```bash
python worker.py
```

### Client side
Activate env
```bash
poetry shell
ipython
```

Run this line by line in iPython to test:

```python
# send task request to server
response = requests.post(
    'http://127.0.0.1:5000/multiply',
    json={'x': 2.0, 'y': 3.0}
)

# parse task id from response
task_id = response.json()['task_id']

# prepare and make get result request 
url = f'http://127.0.0.1:5000/multiply/{task_id}'
response = requests.get(url)

# check status
response.status_code  

# when it is 200, show the result
response.json()
```
