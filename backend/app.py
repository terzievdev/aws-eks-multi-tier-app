from flask import Flask, jsonify, request
import redis
import os
import socket

app = Flask(__name__)

# Redis connection
REDIS_HOST = os.getenv('REDIS_HOST', 'redis-service')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

try:
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    redis_client.ping()
    redis_available = True
except:
    redis_available = False

@app.route('/')
def home():
    return jsonify({
        'service': 'Flask Backend API',
        'status': 'healthy',
        'hostname': socket.gethostname(),
        'redis_connected': redis_available
    })

@app.route('/api/counter', methods=['GET', 'POST'])
def counter():
    if not redis_available:
        return jsonify({'error': 'Redis not available'}), 503
    
    if request.method == 'POST':
        count = redis_client.incr('visit_counter')
        return jsonify({'action': 'incremented', 'counter': count})
    else:
        count = redis_client.get('visit_counter') or 0
        return jsonify({'counter': int(count)})

@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
