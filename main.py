from helpers.middleware import setup_metrics
from flask import Flask

app = Flask(__name__)

setup_metrics(app)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

@app.route('/metrics/')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/test/')
def test():
    return 'rest'


@app.route('/test1/')
def test1():
    1/0
    return 'rest'


@app.errorhandler(500)
def handle_500(error):
    return str(error), 500


if __name__ == '__main__':
    app.run()