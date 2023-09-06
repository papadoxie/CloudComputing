#!/usr/bin/env python3
import sys

for line in sys.stdin:
    words = line.strip().split(',')
    movieID = words[1]
    rating = float(words[2])
    print(movieID, '\t', rating)