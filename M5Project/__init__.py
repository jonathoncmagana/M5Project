import argparse


def compare_strings():
    parser = argparse.ArgumentParser()
    parser.add_argument("firstString",  help="the first string") #type=int,
    parser.add_argument("secondString", help="the second string")
    args = parser.parse_args()
    print(f"I will compare {args.firstString} and {args.secondString}. Processing...")

    if (args.firstString == args.secondString):
        print("The strings are the same!")
    elif (str.capitalize(args.firstString) == str.capitalize(args.secondString)):
        print("The strings are the same when capitalized!")
    elif (args.firstString < args.secondString):
        print(f"{args.firstString} is before {args.secondString} alphabetically")
    else:  # (args.firstString > args.secondString):
        print(f"{args.firstString} is after {args.secondString} alphabetically")



