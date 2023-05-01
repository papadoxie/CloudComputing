#!/usr/bin/env python3

class PrimeGenerator:
    primes = []

    def start(self, start, end):
        is_prime = [True] * (end+1)
        is_prime[0], is_prime[1] = False, False
        
        for i in range(2, int(end**0.5)+1):
            if is_prime[i]:
                self.primes.append(i)
                for j in range(i**2, end+1, i):
                    is_prime[j] = False
            
        for i in range(int(end **0.5) + 1, end+1):
            if is_prime[i]:
                self.primes.append(i)
            
    def get(self):
        return self.primes