#!/usr/bin/python3
import sys
import signal
import re

# Signal handler for keyboard interruption


def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# Regular expression for matching the log format
line_pattern = re.compile((
    r'^(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - '  # Match IP address
    r'\[(?P<date>[^\]]+)\] '                 # Match date
    r'"GET /projects/260 HTTP/1\.1" '       # Match request line
    r'(?P<status_code>\d{3}) '               # Match status code
    r'(?P<file_size>\d+)$'                   # Match file size
))

# Global variables to store metrics
total_file_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
    }
line_count = 0


def print_metrics():
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


def process_line(line):
    global total_file_size, line_count

    match = line_pattern.match(line)
    if match:
        status_code = int(match.group('status_code'))
        file_size = int(match.group('file_size'))

        # Update metrics
        total_file_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()


def read_lines():
    for line in sys.stdin:
        process_line(line)


if __name__ == "__main__":
    read_lines()
