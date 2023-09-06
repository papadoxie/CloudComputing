#!/usr/bin/env python3
import sys
import json

negative_words = []
with open('negative_words.txt') as f:
    negative_words = f.read().splitlines()

positive_words = []
with open('positive_words.txt') as f:
    positive_words = f.read().splitlines()
    
stop_words = []
with open('stop_words.txt') as f:
    stop_words = f.read().splitlines()

for line in sys.stdin:
    decoded = None
    try:
        decoded = json.loads(line)
    except json.decoder.JSONDecodeError:
        continue
    
    if decoded['_id'] is None:
        continue
    uid = decoded['_id']['$oid']
    
    if decoded['social_feed'] is None:
        continue
    words = decoded['social_feed'].strip().split()
    
    positive = 0
    negative = 0
    
    for word in words:
        if word in positive_words:
            positive += 1
        elif word in negative_words:
            negative += 1
        
    print(uid, '\t', positive, '\t', negative, '\t', line)
       