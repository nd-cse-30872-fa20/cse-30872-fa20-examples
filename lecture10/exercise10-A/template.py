#!/usr/bin/env python3

import collections
import sys

# Functions

def is_palindromic(s):
    # TODO
    return False

# Main Execution

if __name__ == '__main__':
    for word in sys.stdin:
        print('Yes' if is_palindromic(word.rstrip()) else 'No')
