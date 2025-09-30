import re 
def isNumber(tok):
    patern=re.compile(r'[+-]?(?:\d+(?:[.,]\d+)?|[.,]\d+)'
    )
    if re.fullmatch(patern,tok):
        return True
    return False