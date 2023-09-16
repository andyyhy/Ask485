"""Get."""


import re
import math
import flask
from index import STOPWORDS, INVERTED_INDEX, PAGERANK, app


@app.route('/api/v1/')
def get_resource():
    """Return a list of services available."""
    context = {
        "hits": "/api/v1/hits/",
        "url": "/api/v1/"
    }
    return flask.jsonify(**context)


@app.route('/api/v1/hits/')
def get_query():
    """Get query."""
    query = flask.request.args.get("q")
    if flask.request.args.get("w") is None:
        weight = 0.5
    else:
        weight = float(flask.request.args.get("w"))

    # Clean Query
    query = re.sub(r"[^a-zA-Z0-9 ]+", "", query)
    query = query.casefold()
    query = query.split()
    clean_words = []
    for word in query:
        if word not in STOPWORDS:
            clean_words.append(word)

    # Check if all words are in index
    for word in clean_words:
        if word not in INVERTED_INDEX:
            context = {
                "hits": []
            }
            return flask.jsonify(**context)

    # Find docs
    doc_ids = []
    for word in clean_words:
        for doc_id in INVERTED_INDEX[word].keys():
            if doc_id != "idf":
                doc_ids.append(doc_id)

    doc_ids = [i for i in doc_ids if doc_ids.count(i) >= len(clean_words)]
    doc_ids = [*set(doc_ids)]

    temp_list = []
    for doc_id in doc_ids:
        # Calculate score
        q_vector = []
        d_vector = []
        for word in clean_words:
            q_vector.append(INVERTED_INDEX[word]["idf"] * query.count(word))
            d_vector.append(INVERTED_INDEX[word]["idf"] *
                            INVERTED_INDEX[word][doc_id]["tf"])
        q_norm = math.sqrt(sum(i ** 2 for i in q_vector))
        d_norm = math.sqrt(
            INVERTED_INDEX[clean_words[0]][doc_id]["normalization_factor"])

        dot_product = sum(x*y for x, y in zip(q_vector, d_vector))
        tfidf = dot_product / (q_norm * d_norm)

        weighted_score = (weight * PAGERANK[doc_id]) + (1-weight)*(tfidf)
        temp_list.append({
            "docid": doc_id,
            "score": weighted_score
        })

    context = {
        "hits": sorted(temp_list, key=lambda d: d["score"], reverse=True)
    }

    return flask.jsonify(**context)
