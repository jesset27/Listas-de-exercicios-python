'''22. Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Faça um programa que
 receba o valor do salário mínimo e a quantidade de quilowatts consumida por uma residência. 
 Calcule e mostre:
o valor de cada quilowatt;
o valor a ser pago por essa residência;
o valor a ser pago com desconto de 15%.'''
#saida
salario = float(input("Informe o sálario: "))
quantidade_quilowatts = float(input("Informe a quantidade de quilowatts: "))
#processamento
valor_de_quilowatts = salario / 5
valor_em_reais = valor_de_quilowatts * quantidade_quilowatts
valor_descontado = valor_em_reais * 15 / 100
valor_com_desconto = valor_em_reais - valor_descontado
#saida
print("Valor de quilowatts: ",valor_de_quilowatts)
print("Valor em reais: ",valor_em_reais)
print("Valor com desconto: ",valor_com_desconto)