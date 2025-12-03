"""
Advent of Code 2024 - Day 1
"""

import os
import sys

# Add parent directories to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils.helpers import print_answer, read_input


def part1(data):
    """Solve part 1 of the challenge."""

    current_position = 50
    count = 0
    for instruction in data:
        # Parse instruction from string, e.g. extract "L10" -> ("L", 10)
        direction, distance = instruction[0], instruction[1:]
        distance = int(distance)

        if current_position == 0:
            count += 1

        if direction == "L":
            current_position = (current_position - distance) % 100
        else:
            current_position = (current_position + distance) % 100

    return count


def part2(data):
    """Solve part 2 of the challenge."""

    current_position = 50
    count = 0
    for instruction in data:
        # Parse instruction from string, e.g. extract "L10" -> ("L", 10)
        direction, distance = instruction[0], instruction[1:]
        distance = int(distance)

        # Calculate virtual positions (not mod 100) to count zero crossings
        if direction == "L":
            start_virtual = current_position
            end_virtual = current_position - distance
            # Count multiples of 100 crossed when moving left (excluding start)
            count += (start_virtual - 1) // 100 - (end_virtual - 1) // 100
            current_position = end_virtual % 100
        else:
            start_virtual = current_position
            end_virtual = current_position + distance
            # Count multiples of 100 crossed when moving right (excluding start)
            count += end_virtual // 100 - start_virtual // 100
            current_position = end_virtual % 100

    return count


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
