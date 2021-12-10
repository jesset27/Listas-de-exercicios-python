'''30. Faça um programa que receba de um produto:
    o preço
    o tipo (A — alimentação; L — limpeza; e V — vestuário)
    a refrigeração (S — produto que necessita de refrigeração; e N — produto que não necessita de 
    refrigeração) .
Suponha que haverá apenas a digitação de dados válidos e, quando houver digitação de letras, 
utilize maiúsculas. Calcule e mostre:

O valor adicional, de acordo com a tabela a seguir:
REFRIGERAÇÃO	TIPO	PREÇO	        VALOR ADICIONAL
N	            A	    < 15,00	        2,00
                        >= 15,00	    5,00
---------	--------------	-------------------------------
                L	    < 10,00	        1,50
                        >= 10,00	    2,50
---------	--------------	-------------------------------
                V	    < 30,00	        3,00
                        >= 30,00	    2,50
--------------------------	---------	--------------	-------------------------------
S	            A		                8,00
                L		                0,00
                V		                0,00


O valor do imposto, de acordo com a regra a seguir.

PREÇO	        PERCENTUAL SOBRE O PREÇO
< 25,00	        5%
>= 25,00	    8%

O preço de custo, ou seja, preço mais imposto. O desconto, de acordo com a regra a seguir.

O produto que não preencher nenhum dos requisitos a seguir terá desconto de 3%, caso contrário, 0 (zero). Os requisitos são:

Tipo: A

Refrigeração: S

O novo preço, ou seja, preço de custo mais adicional menos desconto.

A classificação, de acordo com a regra a seguir.

NOVO PREÇO	            CLASSIFICAÇÃO
<= 50,00	            Barato
Entre 50,00 e 100,00	Normal
>= 100,00	            Caro
'''

preco = float(input('Digite o preço: '))
tipo = str(input('Digite o tipo A, L OU V: '))
refrig = str(input('Digite se precisa de refrigeração S ou N: '))
if refrig == "N":
    if tipo == "A":
        if preco < 15:
           valor_adic = 2
        else: 
           valor_adic = 5
if tipo == "L":
        if preco < 10:
           valor_adic = 1.5
        else: 
           valor_adic = 2.5
if tipo == "V":
        if preco < 30:
           valor_adic = 3
        else: 
           valor_adic = 2.5
if tipo == "A":
    valor_adic = 8
    if tipo == "L":
        valor_adic = 0
    if tipo == "V":
        valor_adic = 0
print('Valor adicional: ', valor_adic) 

if preco < 25:
    imposto = 5/100 * preco
else:
    imposto = 8/100 * preco 
    print('Impostos:' , imposto)
    pre_custo = preco + imposto
    print('Pre custo:', pre_custo) 

if tipo != "A" and refrig != "S":
  desconto = 3/100 * pre_custo
else:
  desconto = 0
print('Desconto:', desconto) 
novo_pre = pre_custo + valor_adic - desconto
print('Novo preço:', novo_pre) 
if novo_pre <= 50:
    print('Barato')
elif novo_pre < 100:
    print('Normal')
else:
    print('Caro')