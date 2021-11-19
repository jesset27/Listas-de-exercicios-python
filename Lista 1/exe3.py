"""
3. Faça um programa que receba três notas, calcule e mostre a média aritmética.
LEIA nota1, nota2, nota3
media = (nota1 + nota2 + nota3) / 3
ESCREVA media
"""
#entrada
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
#processamento
media = ( nota1 + nota2 + nota3 ) / 3
#saída
print('Média: ',media)