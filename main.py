import json
from flask import Flask, render_template, jsonify

from aggregate import search, missing_agg_query, all_source_counts

app = Flask(__name__)


SHARE_API_URL = 'https://osf.io/api/v1/share/search/?raw=True&v=2'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/data/')
def get_data():
    aggs = all_source_counts()
    results = search(SHARE_API_URL, aggs)

    return jsonify(results)


@app.route('/sources')
def term_query():

    return render_template('charts.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
