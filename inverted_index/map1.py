#!/usr/bin/env python3
"""Map 1 - [doc_id, doc_title, doc_body] --> [word, doc_id], [tfik]."""
import sys
import csv
import re


csv.field_size_limit(sys.maxsize)
with open('stopwords.txt', "r", encoding="utf-8") as file:
    stop_words = set(file.read().split())

for row in csv.reader(sys.stdin):
    doc_id = row[0]
    title_and_body = row[1] + ' ' + row[2]
    title_and_body = re.sub(r"[^a-zA-Z0-9 ]+", "", title_and_body)
    title_and_body = title_and_body.casefold()
    words = title_and_body.split()
    for word in words:
        if word not in stop_words:
            print(f'{word} {doc_id}\t1')
