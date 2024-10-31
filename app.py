from flask import Flask, request, jsonify
import os
import signal
import time

app = Flask(__name__)


# GET request to return "bar"
@app.route('/foo', methods=['GET'])
def foo():
    return 'bar', 200


# POST request to return a greeting
@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    name = data.get('name', 'World')
    return f'Hello {name}!', 200


# GET request to kill the container
@app.route('/kill', methods=['GET'])
def kill():
    os.kill(os.getpid(), signal.SIGINT)  # Kill the current process
    return 'Shutting down', 200


DATA_FILE = '/data/saved_string.txt'


# Request to save a string
@app.route('/saveString', methods=['POST'])
def save_string():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    data = request.get_json()
    string_to_save = data.get('data', 'defaultString')
    with open(DATA_FILE, 'w') as f:
        f.write(string_to_save)
    return 'String saved!', 200


# Request to retrieve the saved string
@app.route('/getString', methods=['GET'])
def get_string():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            saved_string = f.read()
        return saved_string, 200
    return 'No string saved yet.', 404


# Simulate high CPU usage
@app.route('/busywait', methods=['GET'])
def busy_wait():
    start_time = time.time()
    while time.time() - start_time < 180:
        a = [x**2 for x in range(1000)]
    return 'CPU intensive task completed', 200


# Health check endpoint
@app.route('/isAlive', methods=['GET'])
def is_alive():
    return 'true', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30000)
