#!/usr/bin/env python3
import sys

ID = None
total = 0
num = 0

for line in sys.stdin:
    movieId, rating = line.strip().split()
    rating = float(rating)
    
    if ID == movieId:
        total += rating
        num += 1
        continue 
    
    if ID:
        print(ID, '\t', total/num)
        
    ID = movieId
    total = rating
    num = 1