#!/usr/bin/env python3
"""Map 2."""
import sys

# Mapper output: doc_id    (word, wordcount)

for line in sys.stdin:
    word, doc_id, wordcount = line.split()
    print(f"{word}\t{doc_id} {wordcount} 1")
