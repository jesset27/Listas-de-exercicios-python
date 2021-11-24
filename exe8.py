'''8. Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e 
mostre o valor do rendimento e o valor total depois do rendimento de um mês.'''

#entrada
deposito = float(input('valor de deposito: '))
juros = float(input("Taxa de juros: "))
#processamento
rendimento = deposito * juros / 100
total = deposito + rendimento
#saida
print("Rendimento: ",rendimento)
print("Valor total: ",total)