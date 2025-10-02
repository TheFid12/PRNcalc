def schet(pop1, pop2, op):
    """Выполняет арифметическую операцию над двумя числами.


Args:
pop1 (str): Первый операнд (строкой).
pop2 (str): Второй операнд (строкой).
op (str): Оператор (+, -, *, /, //, %, **).


Returns:
float | int: Результат операции.
"""
    match op:
                case '+':
                    res = float(pop1) + float(pop2)
                case '-':
                    res = float(pop2) - float(pop1)
                case '*':
                    res = float(pop1) * float(pop2)
                case '/':
                    try:
                         res = float(pop2) / float(pop1)
                    except ZeroDivisionError:
                         print("Деление на 0 невозможно")
                         exit(1)
                case '**':
                    res= float(pop2)**float(pop1)
                case '//':
                    try:
                        res=int(pop2)//int(pop1)
                    except ValueError:
                         print("Операции // и % только для целых чисел")
                         exit(1)
                    except ZeroDivisionError:
                         print("Деление на 0 невозможно")
                         exit(1)
                case '%':
                    try:
                        res=int(pop2)%int(pop1)
                    except ValueError:
                         print("Операции // и % только для целых чисел")
                         exit(1)
                case _:
                    raise SyntaxError("Неизвестная операция")
    return res
