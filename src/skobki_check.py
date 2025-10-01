from prnv import check_rpn


def check_skobki(tokens):
    i = 0
    stack = []
    while i < len(tokens):
        if tokens[i] == '(':
            stack.append(i)
        elif tokens[i] == ')':
            if not stack:
                return False
            start = stack.pop()
            if not check_skobki(tokens[start+1:i]):
                return False
            if not check_rpn([t for t in tokens[start+1:i] 
                              if t not in {'(', ')'}],0):
                return False
        i += 1
    return not stack