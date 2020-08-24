#!/usr/bin/env python3

# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import sys

# Functions

def phone_combinations(numbers, letters):
    # TODO: Recursively generate combinations
    pass

# Main Execution

def main():
    for numbers in sys.stdin:
        for combination in phone_combinations(numbers.strip(), ''):
            print(combination)

if __name__ == '__main__':
    main()
