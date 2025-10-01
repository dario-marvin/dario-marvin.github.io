from typing import List
from math import sqrt, ceil

# Naive algorithm
# Algorithm time complexity: O(n * sqrt(n))

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if (n == 2) | (n == 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def primes_naive(n: int) -> List[int]:
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes


# Pure Python sieve of Eratosthenes
# Algorithm time complexity: O(sqrt(n) * log log n)))

def sieve_eratosthenes(n: int) -> List[int]:
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]
    

# Sieve with numpy acceleration

def primesfrom2to(n: int) -> List[int]:
    sieve = np.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return list(np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)])
