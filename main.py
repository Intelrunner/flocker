# Outcome: load simple webpage
import datetime

from flask import Flask, render_template
from google.cloud import firestore
import datetime
import uuid

app = Flask(__name__)

# Add new document

db = firestore.Client()
doc_ref = db.collection(u'times').document(str(x))


def store_time():
    x = datetime.datetime.now()
    v = uuid.uuid1()
    return doc_ref.set({u'id': str(v), u'timestamp': x})


def fetch_times():
    query = db.collection(u'times').order_by(u'timestamps').limit(10).stream
    return query


@app.route('/writetimes')
def root():
    query = db.collection(u'times').order_by(u'timestamps').limit(10).stream
    return render_template('index.html', times=query)


@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps\

    dummy_times = [
        datetime.datetime(2018, 1, 1, 10, 0, 0),
        datetime.datetime(2018, 1, 2, 10, 30, 0),
        datetime.datetime(2018, 1, 3, 11, 0, 0),
    ]

    return render_template('index.html', times=dummy_times)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    app.run(host='127.0.0.1', port=8080, debug=True)