"""
Common helper functions for Advent of Code solutions.
"""

import inspect
import os


def _resolve_path(file_path: str) -> str:
    """Resolve file path relative to the calling script's directory."""
    if os.path.isabs(file_path):
        return file_path

    # Get the caller's file path (skip helper functions in this module)
    stack = inspect.stack()
    helpers_dir = os.path.dirname(os.path.abspath(__file__))
    for frame_info in stack[1:]:  # Skip _resolve_path itself
        caller_file = frame_info.filename
        caller_dir = os.path.dirname(os.path.abspath(caller_file))
        # Use first frame that's not in the helpers module
        if caller_dir != helpers_dir:
            return os.path.join(caller_dir, file_path)

    # Fallback to current working directory if we can't find caller
    return file_path


def read_input(file_path: str = "input.txt") -> list[str]:
    """Read input file and return lines as a list of strings."""
    resolved_path = _resolve_path(file_path)
    with open(resolved_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def read_input_raw(file_path: str = "input.txt") -> str:
    """Read input file and return as a single string."""
    resolved_path = _resolve_path(file_path)
    with open(resolved_path, "r") as f:
        return f.read().strip()


def read_input_ints(file_path: str = "input.txt") -> list[int]:
    """Read input file and return lines as a list of integers."""
    resolved_path = _resolve_path(file_path)
    with open(resolved_path, "r") as f:
        return [int(line.strip()) for line in f.readlines() if line.strip()]


def read_input_grid(file_path: str = "input.txt") -> list[list[str]]:
    """Read input file and return as a 2D grid (list of lists)."""
    resolved_path = _resolve_path(file_path)
    with open(resolved_path, "r") as f:
        return [list(line.strip()) for line in f.readlines()]


def print_answer(part: int, answer: any) -> None:
    """Print the answer in a formatted way."""
    print(f"Part {part}: {answer}")
