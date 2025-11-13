# text_utils.py
import time
import sys

def slow_print(text, delay=0.03, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def slow_print_lines(lines, delay=0.03, line_pause=0.5):
    """
    Print multiple lines with delay, pausing between lines.
    
    Args:
        lines: List of text lines to print
        delay: Delay between each character
        line_pause: Pause between lines in seconds
    """
    for line in lines:
        slow_print(line, delay=delay)
        time.sleep(line_pause)