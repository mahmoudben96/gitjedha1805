# example_argparse.py
import argparse

def main():
    parser = argparse.ArgumentParser(description="Example script with arguments")
    parser.add_argument("arg1", help="The first argument")
    parser.add_argument("arg2", help="The second argument")

    args = parser.parse_args()

    a = float(args.arg1)
    b = int(args.arg2)

    c = a ** b
    print(f"Print the result of {a} to the power {b} is : {c}")

if __name__ == "__main__":
    main()