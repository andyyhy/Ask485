#!/usr/bin/env python3
"""Map 4."""
import sys


# Mapper output: doc_id % 3
# (word, doc_id, wordcount, total_doc_words, num_docs_contain_word)

for line in sys.stdin:
    word, doc_id, wordcount, idf, normalization_factor = line.split()
    temp = int(doc_id) % 3
    print(f"{temp}\t{word} {doc_id} {wordcount} {idf} {normalization_factor}")
