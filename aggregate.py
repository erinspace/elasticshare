from __future__ import division

import requests


# Local settings
# OSF_APP_URL = 'http://localhost:5000/api/v1/share/search/?raw=True'

# production SHARE settings
OSF_APP_URL = 'https://osf.io/api/v1/share/search/?raw=True&v={}'


def query_osf(url, query):
    response = requests.post(url, json=query, verify=False)
    return response.json()


def search(url, aggs):
    query = {
        'size': 0,
        'aggs': aggs
    }

    osf_query = query_osf(url, query)
    return osf_query


def missing_agg_query(terms):
    return {
        "{}MissingAggregation".format(term): {
            "filter": {
                "query": {
                    "query_string": {
                        "query": "NOT {}:*".format(term)
                    }
                }
            },
            "aggs": {
                "sources": {
                    "terms": {
                        "field": "source",
                        "min_doc_count": 0,
                        "size": 0
                    }
                }
            }
        } for term in terms
    }


def all_source_counts():
    return {
        "allSourceAgg": {
            "terms": {
                "field": "source",
                "min_doc_count": 0,
                "size": 0
            }
        }
    }


def includes_agg_query(terms):
    return {
        "{}IncludedAggregation".format(term): {
            "filter": {
                "query": {
                    "query_string": {
                        "query": "{}:*".format(term)
                    }
                }
            },
            "aggs": {
                "sources": {
                    "terms": {
                        "field": "source",
                        "size": 0
                    }
                }
            }
        } for term in terms
    }


def terms_agg_query(terms, size):
    return {
        "{}TermFilter".format(term): {
            "terms": {
                "field": term,
                "size": size,
                "exclude": "of|and|or",
                "size": size
            }
        } for term in terms
    }

