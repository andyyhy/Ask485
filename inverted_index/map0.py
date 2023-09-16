#!/usr/bin/env python3
"""Map 0."""
import sys
import csv

csv.field_size_limit(sys.maxsize)


for row in csv.reader(sys.stdin):
    print(f"1\t{row}")
