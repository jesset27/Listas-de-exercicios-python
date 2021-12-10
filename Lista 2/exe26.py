'''26. Faça um programa que receba:
O código de um produto comprado, supondo que a digitação do código do produto seja sempre 
válida, isto é, um número * inteiro entre 1 e 10.
O peso do produto em quilos.
O código do país de origem, supondo que a digitação do código seja sempre válida, isto é, um 
número inteiro entre 1 e 3.

CÓDIGO DO PAÍS DE ORIGEM	IMPOSTO
1	                        0%
2	                        15%
3	                        25%
CÓDIGO DO PAÍS DO PRODUTO	Preço por grama
1 a 4	                    10
5 a 7	                    25
8 a 10	                    35

Calcule e mostre:

o peso do produto convertido em gramas;
o preço total do produto comprado;
valor do imposto, sabendo que ele é cobrado sobre o * preço total do produto comprado e dependendo país de origem;
o valor total, preço total do produto mais imposto.
'''

codigo_produto = int(input("Código do produto: "))
peso_quilos = float(input("Peso em quilos: "))
codigo_pais = int(input("Código do país: "))
peso_em_gramas = peso_quilos * 1000
print("Peso do produto em gramas: ",peso_em_gramas)
if codigo_produto >= 1 and codigo_produto <= 4:
   preco_por_grama = 10
elif codigo_produto >= 5 and codigo_produto <= 7:
   preco_por_grama = 25
elif codigo_produto >= 8 and codigo_produto <= 10:
   preco_por_grama = 35    
preco_total = peso_em_gramas * preco_por_grama
print("Preço total: ",preco_total)
if codigo_pais == 1:
    imposto = 0
elif codigo_pais == 2:
    imposto = preco_total * 15/100
elif codigo_pais == 3:
    imposto = preco_total * 25/100    
print("Valor do imposto: ",imposto)
valor_total = preco_total + imposto
print("Valor total: ",valor_total)