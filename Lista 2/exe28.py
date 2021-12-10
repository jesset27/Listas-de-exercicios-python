'''28. Faça um programa que receba o salário base e o tempo de serviço de um funcionário. 
Calcule e mostre:
O imposto, conforme a tabela a seguir.
A gratificação, de acordo com a tabela a seguir.
O salário líquido, ou seja, salário base menos imposto mais gratificação.
A categoria, que está na tabela a seguir.'''

salario_base =  float(input("Salario base: "))
tempo_trabalho = float(input("Tempo de trabalho: "))
if salario_base < 200:
    imposto = 0
elif salario_base <= 450:
    imposto = 3/100 * salario_base
elif salario_base < 700:
    imposto = 8/100 * salario_base
else:
    imposto = 12/100 * salario_base
print("Impostos: ",imposto)
if salario_base > 500:
    if tempo_trabalho <= 3:
         gratificacao = 20
    else: 
        gratificacao = 30
else:
    if tempo_trabalho <= 3:
        gratificacao = 23
    elif tempo_trabalho < 6:
        gratificacao = 35
    else:
        gratificacao = 33
print("Gratificação: ",gratificacao)
salario_liquido = salario_base - imposto + gratificacao
print("Salario_liquido: ",salario_liquido)
if salario_liquido <= 350:
    print("Classificação A")
elif salario_liquido < 600:
    print("Classificação B")
else:
    print("Classificação C")