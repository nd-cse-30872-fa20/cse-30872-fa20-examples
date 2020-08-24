#!/usr/bin/env python3

# Functions

def permutations(p, c):
    if not c:
        print(p)
        return

    for e in sorted(c):
        permutations(p + e, c.difference({e}))

# Main Execution

if __name__ == '__main__':
    permutations('', set('ABC'))
