import  sys
from src.calc import calc


def main() -> None:
    """Главная функция программы.


Читает ввод построчно из stdin и передает его в функцию calc.
"""
    for line in sys.stdin:
        if line.strip().lower() == "exit":
            print("Выход из программы.")
            break
        calc(line.rstrip())




if __name__ == "__main__":
    main()
