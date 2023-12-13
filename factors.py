#!/usr/bin/env python3

import sys

def factorize(number):
    factors = []
    for i in range(2, int(number**0.5) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors

def main(filename):
    with open(filename, 'r') as file:
        content = file.read()

    numbers = [int(num) for num in content.replace('\\n', '\n').split('\n') if num]
    
    for num in numbers:
        factors = factorize(num)
        print(f"{num}={'*'.join(map(str, factors))}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)

