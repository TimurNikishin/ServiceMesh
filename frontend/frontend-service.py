# Save as frontend-service.py
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

backend_url = "http://backend-service:5001/data"

@app.route('/')
def hello():
    response = requests.get(backend_url)
    return f'Frontend: {response.json()["message"]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
