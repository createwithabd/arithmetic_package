# arithmetic.py
import argparse


def add(x, y):
    return x + y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

def main():
    parser = argparse.ArgumentParser(description='My Package')
    parser.add_argument('--num1', required=True, help='First Number')
    parser.add_argument('--num2', required=False, type=int, help='Second Number')

    args = parser.parse_args()
    print(args.num1, args.num2)

if __name__ == '__main__':
    main()