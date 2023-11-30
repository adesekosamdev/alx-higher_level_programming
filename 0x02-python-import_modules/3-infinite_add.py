#!/usr/bin/python3
import sys


def main():
    num_args = len(sys.argv) - 1
    result = 0
    for i in range(1, num_args + 1):
        result = result + int(sys.argv[i])
    print(result)


if __name__ == "__main__":
    main()
