import logging
from flask import Flask, Response, request
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler

app = Flask(__name__)

#/ping
@app.route('/ping')
def ping():
    return 'pong'

#/?region=us-west-2&bucket=tapastic.com&name=/aq23/123/asf/333999.png
@app.route('/')
def s3():
    if 'key' in request.args:
        app.logger.info('%s,%s,%s' % (request.args['region'], request.args['bucket'], request.args['key']))

    return Response('', status=200, mimetype='text/plain')

if __name__ == '__main__':
    # Remove access log.
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    # Set 
    handler = TimedRotatingFileHandler('logs/s3.log', 
                                        when='midnight', 
                                        interval=1, 
                                        backupCount=7)

    handler.setLevel(logging.INFO)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(port=8008)

