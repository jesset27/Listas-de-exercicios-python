'''#### 15. O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual 
de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que 
receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de
 impostos, calcule e mostre:
o valor correspondente ao lucro do distribuidor;
o valor correspondente aos impostos;
o preço final do veículo.'''

#entrada
preco_fabrica = float(input('Preço de fabrica: '))
lucro = float(input('Lucro do distribuidor: '))
imposto = float(input('Imposto do preço de fabrica: '))
#processamento 
lucro = preco_fabrica * lucro / 100
imposto = preco_fabrica * imposto / 100
preco_final = preco_fabrica + lucro + imposto
#saida
print('Lucro distribuido: ',lucro)
print('Valor de imposto: ',imposto)
print('Preço final: ',preco_final)