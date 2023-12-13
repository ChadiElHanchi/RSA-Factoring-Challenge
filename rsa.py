#!/usr/bin/env python3

import sys
import math
import random  # Add this line

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Miller-Rabin primality test
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def find_prime_factor(n):
    if n % 2 == 0:
        return 2

    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0 and is_prime(i):
            return i

    return n

def factorize_rsa(n):
    factors = []
    
    while n > 1:
        prime_factor = find_prime_factor(n)
        factors.append(prime_factor)
        n //= prime_factor

    return factors

def main(filename):
    with open(filename, 'r') as file:
        content = file.read()

    numbers = [int(num) for num in content.replace('\\n', '\n').split('\n') if num]
    
    for num in numbers:
        factors = factorize_rsa(num)
        print(f"{num}={'*'.join(map(str, factors))}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rsa.py <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)

