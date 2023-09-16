#!/usr/bin/env python3
"""Reduce 4."""
import sys
import itertools

# Reducer output:
# word doc_id wordcount total_doc_words num_docs_contain_word


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
    words = {}
    for line in group:
        word, \
            doc_id, \
            wordcount, \
            idf, \
            normalization_factor = line.partition("\t")[
                2].split()

        if word in words:
            words[word] += " " + doc_id + " " + \
                wordcount + " " + normalization_factor
        else:
            words[word] = str(idf)
            words[word] += " " + doc_id + " " + \
                wordcount + " " + normalization_factor

    for word, rest in words.items():
        print(word + " " + rest)


if __name__ == "__main__":
    main()
