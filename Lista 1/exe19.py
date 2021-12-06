'''19. Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura e a 
altura que o usuário deseja alcançar subindo a escada, calcule e mostre quantos degraus ele 
deverá subir para atingir seu objetivo, sem se preocupar com a altura do usuário. Todas as 
medidas fornecidas devem estar em metros.'''
#Observação: o operador // em Python é utilizado para pegar a parte inteira de uma divisão
#entrada
altura_do_degrau = float(input("Altura do degrau em metros: "))
altura_desejada = float(input("Altura desejada em metros: "))
#processamento
quantidade_degraus =  altura_do_degrau // altura_desejada
#saida
print('Quantidade de degraus: ',quantidade_degraus)