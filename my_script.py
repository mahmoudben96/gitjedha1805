# example.py
import sys

def main(args):
    if len(args) != 3:
        print("Usage: python example.py <arg1> <arg2>")
        return

    arg1 = args[1]
    arg2 = args[2]

    print(f"Argument 1: {arg1}")
    print(f"Argument 2: {arg2}")

if __name__ == "__main__":
    main(sys.argv)