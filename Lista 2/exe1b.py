'''1.b) Faça um algoritmo que calcule e exiba o salário reajustado de um funcionário de acordo
 com a seguinte regra: Salário até 500, reajuste de 50%; Salários maiores que 500, reajuste de 
 30%.'''
#entrada
salario = float(input("Informe o salário: "))
#processamento
if salario <=500:
    salario_reajustado = salario + (salario * 50 / 100)
else:
    salario_reajustado = salario + (salario * 30 / 100)
print("Salario reajustado: ",salario_reajustado)