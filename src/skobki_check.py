from src.prnv import check_rpn


def check_skobki(tokens):
    """Проверяет корректность расстановки скобок в выражении.


Args:
tokens (list): Список токенов выражения.


Returns:
bool: True, если скобки корректны, иначе False.
"""
    i = 0
    stack = []
    while i < len(tokens):
        if tokens[i] == '(':
            stack.append(i)
        elif tokens[i] == ')':
            if not stack:
                print("Закрывающия скобка без открывающей")
                return False   
            start = stack.pop()
            if not check_skobki(tokens[start+1:i]):
                return False
            if not check_rpn([t for t in tokens[start+1:i]
                              if t not in {'(', ')'}],0):
                print("Выражение в скобках не является обратной польской записью")
                return False
        i += 1
    if stack:
        print("Открывающих скобок больше чем закрывающих")
    return not stack
