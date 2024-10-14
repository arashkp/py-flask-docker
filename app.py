from flask import Flask, request, jsonify
import os
import signal

app = Flask(__name__)


# Endpoint 1: Simple GET request to return "bar"
@app.route('/foo', methods=['GET'])
def foo():
    return 'bar', 200

# Endpoint 2: POST request to return a greeting with the name provided in the JSON body
@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    name = data.get('name', 'World')
    return f'Hello {name}!', 200

# Endpoint 3: GET request to kill the container
@app.route('/kill', methods=['GET'])
def kill():
    os.kill(os.getpid(), signal.SIGINT)  # Kill the current process
    return 'Shutting down', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)