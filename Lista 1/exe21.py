'''21. Uma pessoa deseja pregar um quadro em uma parede. Faça um programa para calcular e mostrar
a que distância a escada deve estar da parede. A pessoa deve fornecer o tamanho da escada e a 
altura em que deseja pregar o quadro. Lembre-se de que o tamanho da escada deve ser maior que a 
altura que se deseja alcançar.'''
#saida
tamanho_da_escada = float(input("Tamanho da escada: "))
altura_desejada = float(input("Altura desejada: "))
#processamento
y = tamanho_da_escada ** 2 - altura_desejada ** 2
y = y ** (1 / 2)
print("Distância a escada deve estar da parede: ",y)