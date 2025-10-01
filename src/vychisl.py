

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
                         exit(1)
                case '%':
                    try:
                        res=int(pop2)%int(pop1)
                    except ValueError:
                         print("Операции // и % только для целых чисел")  
                         exit(1)                
                case _:
                    raise SyntaxError("Unknown operation")
    return res