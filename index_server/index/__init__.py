"""Insta485 package initializer."""
import os
import pathlib
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

STOPWORDS = set()
INVERTED_INDEX = {}
PAGERANK = {}


def load_inverted_index(path):
    """Load inverted index."""
    with open(path, "r", encoding="utf-8") as file:
        while True:
            line = file.readline().split()
            if not line:
                break
            term = line[0]
            idf = float(line[1])
            info = {}
            for i in range(2, len(line)-2, 3):
                doc_id = int(line[i])
                t_f = line[i+1]
                normalization_factor = line[i+2]
                info[doc_id] = {
                    "tf": int(t_f),
                    "normalization_factor": float(normalization_factor)
                }

            content = {"idf": idf}
            content.update(info)
            INVERTED_INDEX[term] = content


def load_index():
    """Load index."""
    # Load stop words
    with open('index_server/index/stopwords.txt', "r", encoding="utf-8") as file:
        temp = set(file.read().split())
    for word in temp:
        STOPWORDS.add(word)

    # Check if inverted index dir exists
    path = os.path.join(pathlib.Path().resolve(),
                        "index_server/index/inverted_index")

    # Load Inverted_index
    if os.path.exists(path):
        load_inverted_index(os.path.join(path, index.app.config["INDEX_PATH"]))
    else:
        load_inverted_index(index.app.config["INDEX_PATH"])
    # Load Page Rank
    with open("index_server/index/pagerank.out", "r", encoding="utf-8") as file:
        while True:
            line = file.readline().split(",")
            if not line[0]:
                break
            doc_id = int(line[0])
            rest = float(line[1])
            PAGERANK[doc_id] = rest


app.config["INDEX_PATH"] = os.getenv("INDEX_PATH", "inverted_index_1.txt")
import index.api  # noqa: E402  pylint: disable=wrong-import-position

load_index()
