#!/usr/bin/env python3
"""Reduce 3."""
import sys
import itertools

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
    group_list = []
    for line in group:
        group_list.append(line)

    sum_tf_idf_squared = 0
    # Calculate normalization factor for each doc
    for line in group_list:
        tf_idf = float(line.partition("\t")[2].split(
        )[-1]) * float(line.partition("\t")[2].split()[-2])
        sum_tf_idf_squared += (tf_idf**2)
    normalization_factor = sum_tf_idf_squared

    # Output
    for line in group_list:
        word, wordcount, idf = line.partition("\t")[2].split()

        print(f"{word} {key} {wordcount} {idf} {normalization_factor}")


if __name__ == "__main__":
    main()
