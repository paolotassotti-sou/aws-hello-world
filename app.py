from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "message": "Hello from AWS App Runner!",
        "status": "success",
        "environment": "production"
    })

@app.route('/health')
def health_check():
    # Fondamentale per il Load Balancer di AWS
    return "OK", 200

if __name__ == '__main__':
    # Prende la porta dalla variabile d'ambiente PORT (default 8080 per App Runner)
    port = int(os.environ.get('PORT', 8080))
    # host='0.0.0.0' è necessario per accettare traffico esterno al container
    app.run(host='0.0.0.0', port=port)
