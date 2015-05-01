import json
from flask import Flask

from aggregate import search, missing_agg_query

app = Flask(__name__)


SHARE_API_URL = 'https://osf.io/api/v1/share/search/?raw=True&v=2'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/terms')
def term_query():
    aggs = missing_agg_query('description')
    results = search(SHARE_API_URL, aggs)

    return json.dumps(results, indent=4)


if __name__ == '__main__':
    app.debug = True
    app.run()
