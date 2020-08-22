#!/usr/bin/env python3

import sys

# Function

def is_happy(n, seen):
    # TODO
    return False

# Main execution

def main():
    for n in map(int, sys.stdin):
        print('Yes' if is_happy_cached(n, set()) else 'No')

if __name__ == '__main__':
    main()
