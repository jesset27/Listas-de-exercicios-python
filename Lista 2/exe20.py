'''20. Faça um programa que receba o salário inicial de um funcionário, calcule e mostre o novo 
salário, acrescido de bonificação e de auxílio escola.

SALÁRIO	                        BONIFICAÇÃO
Até 500,00	                    5% do salário
Entre 500,00 e 1.200,00	        12% do salário
Acima de 1.200,00	            Sem bonificação


SALÁRIO	            AUXÍLIO ESCOLA
Até 600,00	        150,00
Acima de 600,00	    100,00
novo_salario = salario + bonificacao + auxílio escola'''

salario = float(input("Insira o salario: "))
if salario <= 500:
    bonificacao = salario * 5 / 100
elif salario > 500 and salario <= 1199:
    bonificacao = salario * 12 / 100
elif salario >= 1200:
    print("Sem bonificação")
if salario < 600:
    auxilio_escola = 150
else:
    auxilio_escola = 100
novo_salario = salario + auxilio_escola + bonificacao
print("Salario final: ",novo_salario)