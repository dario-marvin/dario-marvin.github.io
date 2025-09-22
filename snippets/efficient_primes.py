from math import sqrt, ceil
from typing import List


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
    n = int(n)  # in case some float slips in
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


# Sieve of Eratosthenes
# Algorithm time complexity: O(sqrt(n) * log log n)))

def sieve_eratosthenes(n: int) -> List[int]:
    n = int(n)
    sieve = [True] * (n + 1)  # boolean vector of length n
    for i in range(2, n + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False  # flag all multiples of i as non primes
    return [i for (i, p) in enumerate(sieve) if p & (i > 1)]


# Sieve of Atkin
# Theoretical algorithm time complexity: O(n / (log log n))
# Efficient code downloaded from https://web.archive.org/web/20071011180805/http://krenzel.info/static/atkin.py

def sieve_atkin(end: int) -> List[int]:
    end += 1
    lng = int((end/2)-1+end%2)
    sieve = [False]*(lng + 1)

    x_max, x2, xd = int(sqrt((end-1)/4.0)), 0, 4
    for xd in range(4, 8*x_max + 2, 8):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max**2, (y_max << 1) - 1
        if n%2 == 0:
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            m = n%12
            if (m == 1 or m == 5):
                    m = n >> 1
                    sieve[m] = not sieve[m]
            n -= d
                
    x_max, x2, xd = int(sqrt((end-1)/3.0)), 0, 3
    for xd in range(3, 6*x_max + 2, 6):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max**2, (y_max << 1) - 1
        if n%2 == 0:
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            if (n%12 == 7):
                    m = n >> 1
                    sieve[m] = not sieve[m]
            n -= d
                
    x_max, y_min, x2, xd = int((2 + sqrt(4-8*(1-end)))/4), -1, 0, 3
    for x in range(1, x_max + 1):
        x2 += xd
        xd += 6
        if x2 >= end: y_min = (((int(ceil(sqrt(x2 - end))) - 1) << 1) - 2) << 1
        n, n_diff = ((x**2 + x) << 1) - 1, (((x-1) << 1) - 2) << 1
        for d in range(n_diff, y_min, -8):
            if (n%12 == 11):
                    m = n >> 1
                    sieve[m] = not sieve[m]
            n += d

    primes = [2,3]
    if end <= 3 : return primes[:max(0,end-2)]
    
    for n in range(5 >> 1, (int(sqrt(end))+1) >> 1):
        if sieve[n]:
            primes.append((n << 1) + 1)
            for k in range(((n << 1) + 1)**2, end, 2*((n << 1) + 1)**2):
                sieve[k >> 1] = False

    s  = int(sqrt(end)) + 1
    if s%2 == 0: s += 1
    primes.extend([ i for i in range(s, end, 2) if sieve[i >> 1]])
    
    return primes
