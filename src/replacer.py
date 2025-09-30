def replaceunar(expr):
    for i in range(len(expr)):
        expr[i]=expr[i].replace("~", "-")
        expr[i]=expr[i].replace("$", "")
    return expr
