import string, sys
from src.calc import calc


def main() -> None:
    """Главная функция программы.


Читает ввод построчно из stdin и передает его в функцию calc.
"""
    for line in sys.stdin:
        calc(line.rstrip())


    

if __name__ == "__main__":
    main()
