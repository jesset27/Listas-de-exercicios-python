'''23. Faça um programa para resolver equações do 2 o grau.
ax² + bx + c = 0

A variável a deve ser diferente de zero*

delta = b ** 2 - 4 * a * c
delta < 0. Não existe raiz real
delta = 0. Existe uma raiz real
x = (-b) / (2 * a)
delta > 0. Existem duas raízes reais
x1 = (-b + delta )/ (2 * a)
x2 = (-b - delta )/ (2 * a)'''
import math
a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))
delta = b*b - 4 * a * c
if delta < 0:
    print("A equação não possui raizes reais.")
elif delta == 0:
    raiz = (-1*b + math.sqrt(delta))/(2 * a)
    print("A equacao possui apenas uma raiz que e ",raiz)
elif delta > 0:
    raiz1 =(-1*b + math.sqrt(delta))/(2 * a)
    raiz2 =(-1*b - math.sqrt(delta))/(2 * a)
    print("As raizes da equacao sao ",raiz1, "e",raiz2)