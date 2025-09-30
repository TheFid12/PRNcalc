import re


def Tokenxix(expr):
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
