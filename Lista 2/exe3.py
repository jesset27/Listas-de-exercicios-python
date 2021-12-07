'''3. Tendo como dados de entrada a altura e o sexo (M/F) de uma pessoa (M-masculino 
ou F-feminino), construa um algoritmo que calcule seu peso ideal, utilizando as seguintes 
fórmulas:
homem: (72.7 * altura) - 58;

mulher: (62.1 * altura) - 44.7'''
altura = float(input("Informe a altura: "))
sexo = str(input("Informe o sexo: "))
if sexo == "M" or sexo == "m":
    homem = (72.1 * altura) - 58
    print("Peso masculino ideal %.2f" % homem)
elif sexo == "F" or sexo == "f":
    mulher = (62.1 * altura) - 44.7
    print("Peso feminino ideal %.2f" % mulher)