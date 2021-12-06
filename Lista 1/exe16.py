'''16. Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo, 
calcule e mostre o salário a receber, seguindo estas regras:
a hora trabalhada vale a metade do salário mínimo.
o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
o imposto equivale a 3% do salário bruto.
o salário a receber equivale ao salário bruto menos o imposto.'''
#entrada
numerodehorastrabalhadas= float(input('Número de horas trabalhadas: '))
valor_salariominimo = float(input('Salario minimo: '))
#processamento
valor_hora_trabalhada = valor_salariominimo / 2
valor_salario_bruto = valor_hora_trabalhada * numerodehorastrabalhadas
imposto = (valor_salario_bruto * 3) / 100
Valor_salario_liquido =  valor_salario_bruto - imposto
#saida
print('Valor do salario liquido: ',Valor_salario_liquido)