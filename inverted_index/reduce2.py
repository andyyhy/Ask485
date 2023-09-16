#!/usr/bin/env python3
"""Reduce 2."""
import sys
import itertools
import math

# Reducer output: word doc_id wordcount total_doc_words num_docs_contain_word


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def reduce_one_group(key, group):
    """Reduce one group."""
    num_terms = 0
    with open("total_document_count.txt", "r", encoding="utf-8") as file:
        num_terms = int(file.read())

    # Calculate number of docs containing the word
    num_docs = 0
    group_list = list(group)

    for line in group_list:
        count = line.partition("\t")[2].split()[-1]
        num_docs += int(count)

    idf = math.log10(num_terms/num_docs)
    # Output
    for line in group_list:
        doc_id, wordcount, _ = line.partition("\t")[2].split()

        # Calculate idf
        print(f"{key} {doc_id} {wordcount} {idf}")


if __name__ == "__main__":
    main()
