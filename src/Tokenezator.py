import re



def Tokenxix(expr):
    """Разбивает выражение на токены.


Args:
expr (str): Строка с выражением.


Returns:
list: Список токенов.
"""
    pattern = re.compile(
    r"""
    (?:[~$][+-]?\d+(?:\.\d+)?)
    |(?:\d+(?:[.,]\d+)?)
    |//
    |\*\*
    |[+\-*/%()]
    """,
    re.VERBOSE
    )
    tokens = pattern.findall(expr)
    return(tokens)
