#!/usr/bin/env python3
"""Reduce 0."""
import sys
import itertools

# Reducer output: word doc_id wordcount total_doc_words num_docs_contain_word


def main():
    """Divide sorted lines into groups that share a key."""
    for _, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(group)


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def reduce_one_group(group):
    """Reduce one group."""
    # Final output for word
    counter = 0
    for _ in group:
        counter += 1
    print(counter)


if __name__ == "__main__":
    main()
