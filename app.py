from flask import Flask, request, abort
from prometheus_client import start_http_server, Counter, Summary

app = Flask(__name__)


ALLOWED_IPS = ['127.0.0.1', '192.168.0.10' '192.168.219.105' '182.226.37.40' '192.168.180.75'] 


@app.before_request
def limit_remote_addr():
    if request.remote_addr not in ALLOWED_IPS:
        abort(403)  


REQUESTS = Counter('flask_requests_total', 'Total HTTP Requests')
REQUEST_LATENCY = Summary('flask_request_latency_seconds', 'Request latency')


@app.route('/')
def index():
    with REQUEST_LATENCY.time():
        REQUESTS.inc()
        return "Hello, junha !"

@app.route('/hello')
def hello():
    with REQUEST_LATENCY.time():
        REQUESTS.inc()
        return "Come back junha"


if __name__ == '__main__':
    start_http_server(8000)  
    app.run(port=5000, threaded=True)
