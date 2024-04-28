# Save as backend-service.py
from flask import Flask
app = Flask(__name__)

@app.route('/data')
def data():
    return {'message': 'Hello from Backend Service!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
