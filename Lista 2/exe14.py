'''14. Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e os 
dados necessários para executar cada operação.
Menu de opções:
1. Somar dois números.
2. Raiz quadrada de um número.
Observação: raiz = numero ** (1/2), ou import math raiz = math.sqrt(numero)
'''
print("Menu de opções: ")
print("(1) Somar dois números.")
print("(2)Raiz quadrada de um número.")
opcao = input("Insira a opção: ")
if opcao == "1":
    n1 = int(input("Insira o primeiro número: "))
    n2 = int(input("Insira o segundo número: "))
    print("O resultado é:",n1 + n2)
else:
    raiz = int(input("Insira o número: "))
    total = raiz **(1/2)
    print("A raiz de",raiz,"é: ",total)