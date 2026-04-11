import argparse

parser = argparse.ArgumentParser()

# These are positional. 
parser.add_argument("source", help="The file you want to move.")
parser.add_argument("destination", help="Where you want it to go.")

args = parser.parse_args()

print(f"Moving {args.source} to {args.destination}")
