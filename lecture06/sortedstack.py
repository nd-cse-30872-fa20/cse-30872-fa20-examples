#!/usr/bin/env python3

# Functions

def sorted_stack(old_stack):
    new_stack = []
    while old_stack:
        #t = old_stack.pop(0)
        t = old_stack.pop(-1)
        # Go through new stack and copy back over values greater than temporary
        while new_stack and new_stack[-1] > t:
            old_stack.append(new_stack.pop(-1))

        # Place temporary value on top
        new_stack.append(t)
    return new_stack

# Main execution

def main():
    stack = [5, 4, 7, 0, 1]
    print(stack)
    print(sorted_stack(stack))

if __name__ == '__main__':
    main()