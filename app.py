from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <html>
        <head><title>Docker Test App</title></head>
        <body>
            <h1>Hello from Docker!</h1>
            <p>This is a simple Python Flask application running in a Docker container.</p>
            <p>Hostname: {}</p>
        </body>
    </html>
    """.format(os.getenv('HOSTNAME', 'unknown'))

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
