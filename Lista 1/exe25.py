'''25. Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse 
espetáculo. Esse programa deverá calcular e mostrar a quantidade de convites que devem ser 
vendidos para que, pelo menos, o custo do espetáculo seja alcançado.'''
custo = float(input("Digite o custo do evento: "))
convite = float(input("Preço por convite: "))
#processamento
quantidade = custo / convite
#saida
print("Quantidade de convites necessárias para pagar o custo do evento: ",quantidade)