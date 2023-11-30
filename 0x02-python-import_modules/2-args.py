#!/usr/bin/python3
import sys


def main():
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 arguments.")
    else:
        s = "" if num_args == 1 else "s"
        print("{} argument{}:".format(num_args, s))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
