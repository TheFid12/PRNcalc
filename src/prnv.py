from src.isdigit import isnumber
from src.vychisl import schet


def check_rpn(tokens, flag):
    """Проверяет и/или вычисляет выражение в обратной польской нотации.


Args:
tokens (list): Список токенов выражения.
flag (int): 0 — проверка корректности, 1 — вычисление.


Returns:
bool | float: True/False при проверке, либо результат вычисления.
"""
    stacko = []
    for t in tokens:
        if isnumber(t):
            stacko.append(t)
        elif t in {'+', '-', '*', '/', '%', '**', "//"}:
            if len(stacko) < 2:
                return False
            x1=stacko.pop()
            x2=stacko.pop()
            stacko.append(schet(x1,x2,t))
        elif t=='(' or ')':
            continue
        else:
            return False
    if flag==0:
        return len(stacko) == 1
    elif flag==1:
        return stacko.pop()