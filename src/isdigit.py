import re 
def isnumber(tok):
    """Проверяет, является ли токен числом.


Args:
tok (str): Строка для проверки.


Returns:
bool: True, если токен число, иначе False.
"""
    patern=re.compile(r'[+-]?(?:\d+(?:[.,]\d+)?|[.,]\d+)'
    )
    if re.fullmatch(patern,tok):
        return True
    return False