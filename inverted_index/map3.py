#!/usr/bin/env python3
"""Map 3."""
import sys


# Mapper output: doc_id    (word, wordcount, idf)

for line in sys.stdin:
    word, doc_id, wordcount, idf = line.split()
    print(f"{doc_id}\t{word} {wordcount} {idf}")
