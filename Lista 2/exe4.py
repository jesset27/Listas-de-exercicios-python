'''4. Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando 
se este número é par ou ímpar e se é positivo ou negativo.'''
numero = int(input("Indique o numero inteiro:"))
if numero > 0:
    print("Seu número é positivo!")
elif numero == 0:
    print("Número nulo!")
else:
    numero < 0
    print("Seu número é negativo!")
if numero %2 == 0:
    print("Seu número é par!")
else:
    print("Seu número é impar!")