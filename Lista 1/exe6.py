'''6. Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário
 a receber, sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga 
 imposto de 7% também sobre o salário base.'''
 #entrada
salario = float(input('Informe o salario base: '))
#processamento
gratificacao = salario /100 * 5
imposto = salario / 100 * 7
Novo =  ( salario + gratificacao ) - imposto
#saida
print('Salario atual: ',Novo)