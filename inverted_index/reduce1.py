#!/usr/bin/env python3
"""Reduce 1."""
import sys
import itertools

# Reducer output: (word, doc_id)    wordcount


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def reduce_one_group(key, group):
    """Reduce one group."""
    word_count = 0
    for _ in group:
        word_count += 1
    print(f"{key} {word_count}")


if __name__ == "__main__":
    main()
