import sys


def main(argv=None):
    print(f"Start.")
    print(argv)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
