# python3

"""
implement the Rabin–Karp’s algorithm
"""

import random


def hash_str(string, p, x):
    acc = 0
    for c in reversed(string):
        acc = (acc * x + ord(c)) % p
    return acc


def hash_substrings(text, pattern_len, p, x):
    delta = len(text) - pattern_len
    hashes = [0] * (delta + 1)
    i = delta
    last_substring = text[i:]
    hashes[-1] = hash_str(last_substring, p, x)

    y = 1
    for _ in range(pattern_len):
        y = y * x % p

    while i > 0:
        i -= 1
        hashes[i] = (x * hashes[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])) % p

    return hashes


def get_occurences(pattern, text):
    res = []
    prime = 100000000019
    modifier = random.randint(1, prime - 1)
    pattern_len = len(pattern)
    pattern_hash = hash_str(pattern, prime, modifier)
    precomputed_hashes = hash_substrings(text, pattern_len, prime, modifier)

    for i in range(len(precomputed_hashes)):
        if pattern_hash != precomputed_hashes[i]:
            continue

        if pattern == text[i:i + pattern_len]:
            res.append(i)

    return res


def print_occurences(arr):
    print(" ".join(map(str, arr)))


def main():
    pattern = input().rstrip()
    text = input().rstrip()
    print_occurences(get_occurences(pattern, text))


if __name__ == "__main__":
    main()
