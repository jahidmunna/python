import argparse

def arguments():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--input', action='store', type=int, required=True)
    my_parser.add_argument('--id', action='store', type=int)
    return my_parser.parse_args()


if __name__ == "__main__":
    opt = arguments()
    print(f"input: {opt.input} id:{opt.id}")
