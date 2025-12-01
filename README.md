# Advent of Code

Solutions for Advent of Code challenges

## Structure

```
Advent of Code/
├── README.md           # This file
├── utils/              # Common utilities and helpers
│   ├── __init__.py
│   └── helpers.py      # Shared helper functions
├── 2025/               # Year 2025 solutions
│   ├── day01/
│   │   ├── solution.py
│   │   ├── input.txt
│   │   └── README.md   # Optional: notes for this day
│   ├── day02/
│   └── ...
├── 2024/               # Year 2024 solutions
│   ├── day01/
│   └── ...
└── ...
```

## Usage

1. Navigate to the year and day you want to work on:

   ```bash
   cd 2025/day01
   ```

2. Add input from Advent of Code to `input.txt`

3. Implement the solution in `solution.py`

4. Run the solution:

   ```bash
   python solution.py
   ```

## Creating a New Day

1. Create a new directory: `mkdir <year>/day<NN>`
2. Copy the template from `utils/template.py` or create your own
3. Add your input to `input.txt`
4. Start coding!

## Notes

- Each day is self-contained in its own folder
- Common utilities are in the `utils/` directory
- Feel free to use any programming language (Python is just the default template)
