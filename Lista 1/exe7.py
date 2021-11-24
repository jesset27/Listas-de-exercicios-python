'''7. Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário
 a receber, sabendo-se que o funcionário tem gratificação de 50,00 sobre o salário base e paga
  imposto que deve ser lido e é aplicado sobre o salário base.'''

#entrada
salario = float(input('Informe o salario base: '))
imposto = float(input('Informe o impostoem em centagem: '))
#processamento
gratificacao = 50
imposto = ( salario * imposto / 100 )
Novo =  ( salario + gratificacao ) - imposto
#saida
print('Salario a receber: ',Novo)