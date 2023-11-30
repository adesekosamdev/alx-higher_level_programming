#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    num_args = len(sys.argv) - 1
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator_array = ["+", "-", "*", "/"]
        func_array = [add, sub, mul, div]
        if operator not in operator_array:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            index = operator_array.index(operator)
            print("{} {} {} = {}".format(a, operator,
                                         b, func_array[index](a, b)))


if __name__ == "__main__":
    main()
