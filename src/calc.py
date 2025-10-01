from Tokenezator import Tokenxix
from isdigit import isNumber
from replacer import replaceunar
from vychisl import schet
from skobki_check import check_skobki
from prnv import check_rpn

def calc(expr):
    stack=[]
    tokens=Tokenxix(expr)
    while tok := tokens:
        stack.append(tok[0])
        tokens=tokens[1:]
    stack=replaceunar(stack)
    if check_skobki(stack) and check_rpn(stack, 0):
        print(check_rpn(stack, 1)) 




