"""
Advent of Code Solution Template
Copy this file to your day folder and rename it to solution.py
"""

import os
import sys

# Add parent directories to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils.helpers import print_answer, read_input


def part1(data):
    """Solve part 1 of the challenge."""
    # TODO: Implement part 1
    pass


def part2(data):
    """Solve part 2 of the challenge."""
    # TODO: Implement part 2
    pass


def main():
    # Read input
    data = read_input()
    # Or use: data = read_input_raw() for single string
    # Or use: data = read_input_ints() for integers

    # Solve parts
    result1 = part1(data)
    result2 = part2(data)

    # Print answers
    print_answer(1, result1)
    print_answer(2, result2)


if __name__ == "__main__":
    main()
