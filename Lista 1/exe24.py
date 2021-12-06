'''24. Faça um programa que receba uma hora formada por hora e minutos (um número real), calcule
e mostre a hora digitada apenas em minutos. Lembre-se de que:
para quatro e meia, deve-se digitar 4.30;
os minutos vão de 0 a 59.'''
#entrada
hora = float(input("Valor da hora: "))
#processamento
h = hora // 1
minutos = hora - h
conversao = (h * 60) + (minutos * 100)
print("Conversão:",conversao)