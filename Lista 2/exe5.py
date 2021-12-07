'''5. Elabore um algoritmo que informando a idade de um nadador o mesmo terá condições de 
classificar em uma das seguintes categorias:
infantil = 5 - 10 anos;

juvenil = 11-17 anos;

adulto = maiores de 18 anos.'''
idade = int(input("Indique a idade:"))
if idade <= 4:
    print("Sua categoria é indefinida!")
elif idade >=5 and idade <=10:
    print("Sua categoria é infantil!")
elif idade >=11 and idade <=17:
    print("Sua categora é juvenil!")
else:
    idade >= 18
    print("Sua categoria é adulto")