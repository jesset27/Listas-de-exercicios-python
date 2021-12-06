'''23. Faça um programa que receba um número real, encontre e mostre:
a parte inteira desse número;
a parte fracionária desse número;
o arredondamento desse número.
Observação: Para arredondar um número em Python, usa-se a função round(numero), onde se o número 
real/float estiver em igual distância entre o inteiro de cima e o inteiro de baixo, esta função
arredonda para o número par mais próximo.'''
#entrada
numero = float(input("Informe o número: "))
#processamento
parte_inteira = numero // 1
parte_fracionaria = numero - parte_inteira
numero_arredondado = round(numero)
#saida
print("Parte inteira: ",parte_inteira)
print("Parte fracionaria: ",parte_fracionaria)
print("Número arredondado: ",numero_arredondado)