#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    print(line)
    uid, positive, negative, line = line.split(maxsplit=3)
        
    positive = int(positive)
    negative = int(negative)
    
    score = (positive - negative) / (positive + negative + 1)
    
    sentiment = 'neutral'
    if score > 0:
        sentiment = 'positive'
    elif score < 0:
        sentiment = 'negative'
        
    try:
        decoded = json.loads(line)
        decoded['sentiment'] = sentiment
        line = json.dumps(decoded)
        print(line)  
    except json.decoder.JSONDecodeError:
        pass
    