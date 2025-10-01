import string, sys
from calc import calc


def main() -> None:
    for line in sys.stdin:
        calc(line.rstrip())


    

if __name__ == "__main__":
    main()
