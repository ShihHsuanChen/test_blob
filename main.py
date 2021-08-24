from flask import Flask
from flask import send_from_directory, Response


app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


if __name__ == '__main__':
    WS_HOST = '0.0.0.0'
    WS_PORT = '5003'

    app.run(host=WS_HOST, port=WS_PORT, threaded=True)
