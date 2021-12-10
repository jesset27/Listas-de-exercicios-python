'''29. Faça um programa que:
receba o valor do salário mínimo,
o turno de trabalho (M — matutino; V — vespertino; ou N — noturno),
a categoria (O — operário; G — gerente)
número de horas trabalhadas no mês de um funcionário.
Suponha a digitação apenas de dados válidos e, quando houver digitação de letras, utilize maiúsculas.

Calcule e mostre:

O coeficiente do salário, de acordo com a tabela a seguir.
TURNO DE TRABALHO	VALOR DO COEFICIENTE
M - Matutino	    10% do salário mínimo
V - Vespertino	    15% do salário mínimo
N - Noturno	        20% do salário mínimo


O valor do salário bruto, ou seja, o número de horas trabalhadas multiplicado pelo valor do coeficiente do salário.

O imposto, de acordo com a tabela a seguir.

CATEGORIA	    SALÁRIO BRUTO	IMPOSTO SOBRE O SALÁRIO BRUTO
O - Operário	>= 300,00	    5%
O - Operário	< 300,00	    3%
G - Gerente	    >= 300,00	    6%
G - Gerente	    < 300,00	    4%

A gratificação, de acordo com as regras a seguir. Se o funcionário preencher todos os requisitos a seguir, sua gratificação será de 50,00; caso contrário, será de 30,00. Os requisitos são:
    Turno: Noturno
    Número de horas trabalhadas: Superior a 80 horas
    O auxílio alimentação, de acordo com as seguintes regras.
Auxilio alimentação, um terço do seu salário bruto; caso contrário, será de metade do seu salário bruto. Os requisitos são:
    Se o funcionário preencher algum dos requisitos a seguir, seu auxílio alimentação será de
    Categoria: Operário
    Coeficiente do salário: < = 25
O salário líquido, ou seja, salário bruto menos imposto mais gratificação mais auxílio alimentação.
A classificação, de acordo com a tabela a seguir:


SALÁRIO LÍQUIDO	    MENSAGEM
Menor que 350,00	Mal remunerado
Entre 350 e 600,00	Normal
Maior que 600,00	Bem remunerado 
'''

salario_minino = float(input('Informe o salario: '))
turno = str(input('Informe o Turno M, V ou N: '))
categoria = str(input('Informe a categoria G ou O: '))
numero_de_horas_trabalhadas = float(input('Informe o número de horas trabalhadas: '))

if turno == "M":
     coeficiente = 10/100 * salario_minino
elif turno == "V":
     coeficiente = 15/100 * salario_minino
elif  turno == "N":
     coeficiente = 12/100 * salario_minino
print('Coeficiente: ', coeficiente)

salario_bruto = numero_de_horas_trabalhadas * coeficiente
print('Salario Bruto: ', salario_bruto)

if categoria == "O":
    if salario_bruto >= 300:
        imposto = 5/100 * salario_bruto
    else:
        imposto = 3/100 * salario_bruto
else: 
    if salario_bruto >= 400:
        imposto = 6/100 * salario_bruto
    else:
         imposto = 4/100 * salario_bruto
print('Impostos: ' , imposto)

if turno == "N" and numero_de_horas_trabalhadas > 80:
    gratificacao = 50
else:
    gratificacao = 30
 
print('Gratificação: ',  gratificacao )
 
if categoria == "O" or coeficiente <= 25:
    auxilio = 1/3 * salario_bruto
else:
    auxilio = 1/2 * salario_bruto
print('Auxilio:', auxilio)

salario_liquido = salario_bruto - imposto + gratificacao + auxilio
print('Salario liquido:', salario_liquido)

if salario_liquido < 350:
    print("Mal remunerado")
elif salario_liquido >= 350 and salario_liquido <= 600:
     print('Normal')
elif salario_liquido > 600:
     print('Bem remunerado')