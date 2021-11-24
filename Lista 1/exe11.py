'''11. Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
O número digitado ao quadrado

O número digitado ao cubo

A raiz do número digitado

A raiz cúbica do número digitado'''

#entrada
numero = int(input('Digite o número: '))
#processamento
quadrado = numero ** 2
cubo = numero ** 3
raiz_quadrada = numero ** 0.5
raiz_cubica = numero ** 0.33
#saida
print('Quadrado: ',quadrado)
print('Cubo:' ,cubo)
print('Raiz quadrada: ',raiz_quadrada)
print('Raiz cubica: ',raiz_cubica)