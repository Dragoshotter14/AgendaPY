# Calculadora criada por Emerson da Silva Vianna para fins didaticos 26/11/2022 #

######################
import math

def imprimir_menu():
    print("1 - Mais")
    print("2 - Menos")
    print("3 - Divisao")
    print("4 - Multiplicacao")
    print("5 - Equacao do segundo grau")
    print("0 - Fechar Calculadora")

######################
while True:

    imprimir_menu()

    print("----------------------------")
    opcao = input("Digite a opção desejada:")
    print("----------------------------")

    ######################
    if opcao == "1":
        a = float(input("Digite o primeiro numero:"))
        print("----------------------------")
        b = float(input('Digite o segundo numero:'))
        print("----------------------------")
        print(a + b)

    ######################
    elif opcao == "2":
        a = float(input("Digite o primeiro numero:"))
        print("----------------------------")
        b = float(input("Digite o segundo numero:"))
        print("----------------------------")
        print(a-b)
    ######################
    elif opcao == "3":
        a = float(input("Digite o primeiro numero:"))
        print("----------------------------")
        b = float(input("Digite o segundo numero:"))
        print("----------------------------")
        print(a/b)
    ######################
    elif opcao == "4":
        a = float(input("Digite o primeiro numero:"))
        print("----------------------------")
        b = float(input("Digite o segundo numero:"))
        print("----------------------------")
        print(a*b)
    ######################
    elif opcao == "5":
        a = float(input("Digite o valor de a:"))
        print("----------------------------")
        b = float(input("Digite o valor de b:"))
        print("----------------------------")
        c = float(input("Digite o valor de c:"))
        print("----------------------------")
        delta = (b*b-(4*a*c))

        print("O valor de Delta é:", delta)
        print("----------------------------")
        raiz = math.sqrt(delta)
        x1 = ((-b+raiz)/2*a)
        x2 = ((-b-raiz)/2*a)
        print("X1 positivo:", x1)
        print("----------------------------")
        print("X2 negativo:", x2)
        print("----------------------------")
    ######################
    elif opcao == "0":
        print("Saindo da calculadora")
        print("----------------------------")
        break
    ######################
    else:
        print("OPCAO INCORRETA, SAINDO DO PROGRAMA")
        print("----------------------------")
        break
    ######################