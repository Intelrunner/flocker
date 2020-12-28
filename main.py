# Outcome: load simple webpage
from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import uuid
import logging

### firebase init ####
cred = credentials.ApplicationDefault()

firebase_admin.initialize_app(cred, {'projectId': 'eric-playground-298616'})


def get_collection():
    db = firestore.Client()


app = Flask(__name__)


@app.route('/')
def hello():
    x = uuid.uuid1()
    """Return a friendly greeting"""
    return 'Hello World! \n\
        {}'.format(str(x))


@app.route('/test')
def html_test():
    return render_template('index.html')


@app.route('/result')
def result():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('results.html', result=dict)


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
    app.run(host='127.0.0.1', port=8080, debug=True)
