# text_utils.py
import time
import sys

def slow_print(text, delay=0.05, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def scene_header(title, subtitle=None):
    bar = "="*50
    print("\n" + bar)
    print(f"  {title}" + (f"  |  {subtitle}" if subtitle else ""))
    print(bar + "\n")

def pause(prompt="\nPress Enter to continue..."):
    input(prompt)