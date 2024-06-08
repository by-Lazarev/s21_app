import sys
import argparse
import re

def is_valid_line(line):
    """Проверяет, что строка начинается ровно с 5 нулей и имеет длину 32 символа."""
    return re.match(r'^00000.{27}$', line) is not None

def process_lines(num_lines):
    """Обрабатывает строки из стандартного ввода, выводя только корректные строки."""
    lines_processed = 0

    for line in sys.stdin:
        if lines_processed >= num_lines:
            break
        line = line.strip()
        if is_valid_line(line):
            print(line)
            lines_processed += 1  

def main():
    parser = argparse.ArgumentParser(description='Process lines that start with exactly 5 zeroes.')
    parser.add_argument('num_lines', type=int, nargs='?', default=None,
                        help='Number of lines to process from input')
    args = parser.parse_args()

    if args.num_lines is not None:
        process_lines(args.num_lines)
    else:
        for line in sys.stdin:
            line = line.strip()
            if is_valid_line(line):
                print(line)

if __name__ == "__main__":
    main()

