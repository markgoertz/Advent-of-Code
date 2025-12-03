"""
Advent of Code 2025 - Day 3
"""

import os
import sys

# Add parent directories to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils.helpers import print_answer, read_input


def part1(data):
    total = 0
    for line in data:
        max_joltage = 0

        # left pointer starting at the beginning of the line
        for i in range(len(line)):
            # right pointer starting at the next character to the right of the left pointer
            for j in range(i + 1, len(line)):
                print(f"left: {line[i]}, right: {line[j]}")
                n = int(f"{line[i]}{line[j]}")
                if n > max_joltage:
                    max_joltage = n
        print(f"max_joltage: {max_joltage}")
        total += max_joltage
    return total


def part2(data):
    pass


def main():
    # Read input - automatically resolves relative to this script's directory
    data = read_input()

    # Solve parts
    result1 = part1(data)
    result2 = part2(data)

    # Print answers
    print_answer(1, result1)
    print_answer(2, result2)


if __name__ == "__main__":
    main()
