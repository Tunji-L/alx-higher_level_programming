#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    arg_len = len(args)
    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if args[1] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    if args[1] == '+':
        print(f"{args[0]} + {args[2]} = {add(int(args[0]), int(args[2]))}")
    elif args[1] == '-':
        print(f"{args[0]} - {args[2]} = {sub(int(args[0]), int(args[2]))}")
    elif args[1] == '*':
        print(f"{args[0]} * {args[2]} = {mul(int(args[0]), int(args[2]))}")
    else:
        print(f"{args[0]} / {args[2]} = {div(int(args[0]), int(args[2]))}")
