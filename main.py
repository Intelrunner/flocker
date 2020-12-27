# Outcome: load simple webpage
import datetime
from flask import Flask, render_template
from google.cloud import firestore
import datetime
import uuid
import logging

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly greeting"""
    return 'Hello World!'


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error did some shit')
    return """
    An internal and shitty error occured: <pre>{}</pre>
    See logs for a full and complete stack trace.
    """.format(e), 500


if __name__ == '__main__':
    # We use this shit when it runs locally
    # In a 'development' fashion
    # Gunicorn is the standard app server for app engine
    app.run(host='127.0.0.1', post=8080, debug=True)