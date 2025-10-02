def replaceunar(expr):
    """Заменяет операторы '~' и '$', а также ',' на корректные символы.


Args:
expr (list): Список токенов выражения.


Returns:
list: Обновлённый список токенов.
"""
    for i in range(len(expr)):
        expr[i]=expr[i].replace("~", "-")
        expr[i]=expr[i].replace("$", "")
        expr[i]=expr[i].replace(",", ".")
    return expr
