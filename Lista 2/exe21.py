'''21. Faça um programa que receba o valor do salário mínimo, o número de horas trabalhadas, o 
número de dependentes do funcionário e a quantidade de horas extras trabalhadas. Calcule e mostre
o salário a receber do funcionário de acordo com as regras a seguir:

O valor da hora trabalhada é igual a 1/5 do salário mínimo.

O salário do mês é igual ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.

Para cada dependente, acrescentar 32,00.

Para cada hora extra trabalhada, calcular o valor da hora * trabalhada acrescida de 50%.

O salário bruto é igual ao salário do mês mais o valor dos dependentes mais o valor das horas
extras.

Calcular o valor do impostoosto de renda retido na fonte de acordo com a tabela a seguir:

IRFF	    SALÁRIO BRUTO
Isento	    Inferior a 200,00
10%	        De 200,00 até 500,00
20%	        Superior a 500,00

O salário líquido é igual ao salário bruto menos IRRF.

A gratificação é de acordo com a tabela a seguir:

SALÁRIO LÍQUIDO	    GRATIFICAÇÃO
Até 350,00	        100,00
Superior a 350	    50,00
O salário a receber do funcionário é igual ao salário líquido mais a gratificação.'''

salario_minimo = int(input("salário mínimo: "))
numero_horas_trabalhadas = int(input("Horas trabalhadas: "))
numero_dependentes = int(input("Dependentes do funcionário: "))
numero_horas_extras = int(input("Horas extras trabalhadas: "))
valor_hora = 1/5 * salario_minimo
salario_mes = numero_horas_trabalhadas * valor_hora
valor_dependentes = 32 * numero_dependentes
valor_hora_extra = numero_horas_extras * (valor_hora + (valor_hora * 50/100))
salario_bruto = salario_mes + valor_dependentes + valor_hora_extra

if salario_bruto < 200:
    imposto = 0
elif salario_bruto >= 200 and salario_bruto <= 500:
    imposto = salario_bruto * 10/100
elif salario_bruto > 500:
    imposto = salario_bruto * 20/100
salario_liquido = salario_bruto - imposto
if salario_liquido <= 350:
    gratificacao = 100
else:
    gratificacao = 50
salario_a_receber = salario_liquido + gratificacao
print("Salario final",salario_a_receber)