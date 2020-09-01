#!/usr/bin/env python3

# Knight's Dialer
# https://hackernoon.com/google-interview-questions-deconstructed-the-knights-dialer-f780d516f029

import sys

# Functions

NEIGHBORS = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: [],
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}

def dial_numbers(number, length):
    if length == 1:
        yield number
    else:
        for neighbor in NEIGHBORS[number[-1]]:
            yield from dial_numbers(number + [neighbor], length - 1)

def dial_numbers_count(start, length):
    # Base case
    if length == 1:
        return 1
    
    # Recursive step
    return sum(
        dial_numbers_count(neighbor, length - 1) for neighbor in NEIGHBORS[start]
    )

def dial_numbers_count(start, length, cache={}):
    # Base case
    if length == 1:
        return 1
    
    # Memoize recursive step
    pair = (start, length)
    if pair not in cache:
        cache[pair] = sum(
            dial_numbers_count(neighbor, length - 1, cache) for neighbor in NEIGHBORS[start]
        )

    return cache[pair]

def dial_numbers_count(start, length):
    # Initialize Table
    table = [[0 for _ in range(length + 1)] for _ in range(len(NEIGHBORS))]

    # Initialize Base Case: 1 Permutation to Length 1
    for row in range(len(NEIGHBORS)):
        table[row][1] = 1

    # Compute Permutations(Number, Hops):
    #
    #   Permutations(Number, Hops) = Sum(
    #       Permutations(Neighbor, Hops - 1) for Neighbor in Neighbors
    #   )
    for hops in range(2, length + 1):
        for number in range(len(NEIGHBORS)):
            table[number][hops] = sum(table[neighbor][hops - 1] for neighbor in NEIGHBORS[number])

    return table[start][length]

def dial_numbers_count(start, length):
    # Initialize Table and Base Case
    old_table = [1 for _ in range(len(NEIGHBORS))]
    new_table = [1 for _ in range(len(NEIGHBORS))]

    # Compute Permutations(Number, Hops):
    #
    #   Permutations(Number, Hops) = Sum(
    #       Permutations(Neighbor, Hops - 1) for Neighbor in Neighbors
    #   )
    for hops in range(2, length + 1):
        for number in range(len(NEIGHBORS)):
            new_table[number] = sum(old_table[neighbor] for neighbor in NEIGHBORS[number])
        old_table = new_table[:]

    return new_table[start]

# Main Execution

def main():
    for index, line in enumerate(sys.stdin):
        start, length = map(int, line.split())
        numbers       = dial_numbers([start], length)
        count         = dial_numbers_count(start, length)

        if index:
            print()

        print(count)
        for number in sorted(numbers):
            print(''.join(map(str, number)))

if __name__ == '__main__':
    main()
