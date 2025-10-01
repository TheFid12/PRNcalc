from isdigit import isNumber
from vychisl import schet


def check_rpn(tokens, flag):
    stacko = []
    for t in tokens:
        if isNumber(t):
            stacko.append(t)
        elif t in {'+', '-', '*', '/', '%', '**', "//"}:
            if len(stacko) < 2:
                return False
            x1=stacko.pop()
            x2=stacko.pop()
            stacko.append(schet(x1,x2,t))
        else:
            return False
    if flag==0:
        return len(stacko) == 1
    elif flag==1:
        return stacko.pop()