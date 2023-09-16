"""
Search index (main) view.

URLs include:
/
"""
import logging
import heapq
import threading
import requests
import search
from flask import render_template, request


def get_results(url, results, index):
    """Get results."""
    try:
        data = requests.get(url, timeout=10).json()['hits']
        results[index] = data
    except logging.error('Error with URL check!'):

        results[index] = {}
    return True


@search.app.route('/')
def show_home():
    """Show home."""
    args = request.args.to_dict()
    query = args.get('q')
    weight = args.get('w')

    if query is None:
        if weight is None:
            weight = 0.5
        context = {"no_query": True, "weight": weight}
        return render_template("index.html", **context)

    if weight is None:
        q_string = "?q=" + query
        weight = 0.5
    else:
        q_string = "?q=" + query + "&w=" + str(weight)

    # Send request to each index server
    urls = []
    urls.append(search.app.config["SEARCH_INDEX_SEGMENT_API_URLS"][0] +
                q_string)
    urls.append(search.app.config["SEARCH_INDEX_SEGMENT_API_URLS"][1] +
                q_string)
    urls.append(search.app.config["SEARCH_INDEX_SEGMENT_API_URLS"][2] +
                q_string)

    results = [{} for x in urls]
    server0_tread = threading.Thread(
        target=get_results,
        args=(urls[0], results, 0),
    )
    server1_tread = threading.Thread(
        target=get_results,
        args=(urls[1], results, 1),
    )
    server2_tread = threading.Thread(
        target=get_results,
        args=(urls[2], results, 2),
    )

    server0_tread.start()
    server1_tread.start()
    server2_tread.start()

    server0_tread.join()
    server1_tread.join()
    server2_tread.join()

    hits = list(heapq.merge(results[0], results[1], results[2],
                reverse=True, key=lambda v: v['score']))
    hits = hits[:10]

    results_final = []
    # Connect to database
    connection = search.model.get_db()
    for hit in hits:
        cur = connection.execute(
            "SELECT title, summary, url "
            "FROM Documents "
            "WHERE docid = ? ",
            (hit["docid"], )
        )
        results_final.append(cur.fetchall()[0])

    context = {"results": results_final,
               "query_terms": query, "weight": weight}

    return render_template("index.html", **context)
