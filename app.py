from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/data')
def get_data():
    data = {
        'signal_strength': random.uniform(-100, -50),
        'traffic_load': random.uniform(0, 100),
        'latency': random.uniform(10, 100),  # Added latency
        'throughput': random.uniform(10, 1000)  # Added throughput
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)
