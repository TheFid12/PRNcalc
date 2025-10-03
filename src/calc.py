from src.Tokenezator import Tokenxix
from src.replacer import replaceunar
from src.skobki_check import check_skobki
from src.prnv import check_rpn


def calc(expr):
    """Проводит все необходимые проверки и окончательный вывод результата.


Args:
expr (str): Строка с выражением.


Обрабатывает пустой ввод, проверяет скобки и корректность записи.
При корректном выражении выводит результат вычисления.
"""
    if not expr or not expr.split():
        print("Ошибка, Введена пустая строка")
        return 0
    stack=[]
    tokens=Tokenxix(expr)
    while tok := tokens:
        stack.append(tok[0])
        tokens=tokens[1:]
    stack=replaceunar(stack)
    if check_skobki(stack) and check_rpn(stack, 0):
        print(check_rpn(stack, 1))
    elif not check_rpn(stack, 0):
        print("Введеное выражение не является польской записью")
