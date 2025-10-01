

def schet(pop1, pop2, op):
    match op:
                case '+':
                    res = float(pop1) + float(pop2)
                case '-':
                    res = float(pop2) - float(pop1)
                case '*':
                    res = float(pop1) * float(pop2)
                case '/':
                    res = float(pop2) / float(pop1)
                case '**':
                    res= float(pop2)**float(pop1)
                case '//':
                    try:
                        res=int(pop2)//int(pop1)
                    except ValueError:
                         print("Операции // и % только для целых чисел")
                         SystemExit
                case '%':
                    try:
                        res=int(pop2)%int(pop1)
                    except ValueError:
                         print("Операции // и % только для целых чисел")  
                case _:
                    raise SyntaxError("Unknown operation")
    return res