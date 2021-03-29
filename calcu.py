def calculadora():
    print("Calculadora digite a opção correspondente")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Tabuada")
    op = int(input("Digite a opção desejada(1,2,3,4,5): "))
    print("")
    if op == 1:
        print("Você selecionou adição")
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        res = num1 + num2
        print("%s + %s = %s" % (num1, num2, res))
    elif op == 2:
        print("Você selecionou subtração")
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        res = num1 - num2
        print("%s - %s = %s" % (num1, num2, res))
    elif op == 3:
        print("Você selecionou multiplicação")
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        res = num1 * num2
        print("%s x %s = %s" % (num1, num2, res))
    elif op == 4:
        print("Você selecionou divisão")
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        res = num1 / num2
        print("%s / %s = %s" % (num1, num2, res))
    elif op == 5:
        print("Você selecionou tabuada")
        num = int(input("Digite o numero para tabuada: "))
        x = 0
        while x <= 10:
            res = num * x
            print("%s X %s = %s" % (num, x, res))
            x += 1
    else:
        print("A opção digitada não existe")