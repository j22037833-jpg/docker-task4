"""Grade Calculator - a non-web command-line application packaged with Docker."""
import argparse
import platform
import socket
import statistics
import sys

DEFAULT_MARKS = [85, 72, 90, 65]


def classify(average):
    if average >= 80:
        return "High Distinction (HD)"
    if average >= 70:
        return "Distinction (D)"
    if average >= 60:
        return "Credit (C)"
    if average >= 50:
        return "Pass (P)"
    return "Fail (N)"


def main():
    parser = argparse.ArgumentParser(description="Docker CLI Grade Calculator")
    parser.add_argument("marks", nargs="*", type=float,
                        help="task marks between 0 and 100 (default demo marks are used if omitted)")
    args = parser.parse_args()

    marks = args.marks or DEFAULT_MARKS
    if any(m < 0 or m > 100 for m in marks):
        print("Error: every mark must be between 0 and 100.", file=sys.stderr)
        return 1

    average = statistics.mean(marks)
    print("=" * 44)
    print(" Docker CLI Grade Calculator")
    print("=" * 44)
    print(f" Marks entered : {', '.join(f'{m:g}' for m in marks)}")
    print(f" Highest       : {max(marks):g}")
    print(f" Lowest        : {min(marks):g}")
    print(f" Average       : {average:.2f}")
    print(f" Grade         : {classify(average)}")
    print("-" * 44)
    print(f" Container ID  : {socket.gethostname()}")
    print(f" CPU platform  : {platform.machine()}")
    print("=" * 44)
    return 0


if __name__ == "__main__":
    sys.exit(main())
