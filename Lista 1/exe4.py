"""
4. Faça um programa que:
receba o salário de um funcionário
calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.
LEIA salario
novoSalario = salario + (salario * 25 / 100)
ESCREVA novoSalario
"""
#entrada
salario =float(input('Salario atual: '))
#processamento
resultado = salario + (salario * 25 / 100)
#saida
print('Novo Salario: ', resultado)
