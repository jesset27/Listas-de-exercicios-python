"""
5. Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.
LEIA salario, percentual
aumento = salario * percentual/100
ESCREVA aumento
novo_salario = salario + aumento
ESCREVA novo_salario
"""
#entrada
salario = float(input('Informe o salario: '))
aumento= int(input('Aumento em porcentagem: '))
#preocessamento
resultado = salario * (aumento / 100 )
salarioNovo= resultado + salario

#saída
print('Novo salário: ',salarioNovo)
print('Aumento do sálario em porcentagem: ',resultado)