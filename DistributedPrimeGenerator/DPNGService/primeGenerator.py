#!/usr/bin/env python3

class PrimeGenerator:
    primes = []

    def start(self, start, end):
        for i in range(start, end + 1):
            if self.isPrime(i):
                self.primes.append(i)
         
    def isPrime(self, candidate):
        if candidate < 2:
            return False
        for i in range(2, int(candidate ** 0.5) + 1):
            if candidate %  i == 0:
                return False
        return True    
           
    def get(self):
        return self.primes