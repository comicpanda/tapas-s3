import logging,os
from flask import Flask, Response, request
from logging.handlers import TimedRotatingFileHandler

app = Flask(__name__)
res = Response('', status=200, mimetype='text/plain')
#/ping
@app.route('/ping')
def ping():
    return 'pong'

#/?bucket=tapastic.com&name=/aq23/123/asf/333999.png
@app.route('/')
def s3():
    if 'key' in request.args:
        app.logger.info('%s,%s' % (request.args['bucket'], request.args['key']))

    return res

if __name__ == '__main__':
    # Remove access log.
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    # Set 
    handler = TimedRotatingFileHandler(os.path.join(os.path.dirname(__file__), 'logs/s3.log'), 
                                        when='midnight', 
                                        interval=1, 
                                        backupCount=7)

    handler.setLevel(logging.INFO)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port=8008)

