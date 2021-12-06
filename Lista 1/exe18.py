'''18. Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os quais 
fornece a quantidade de ração em gramas. A quantidade diária de ração fornecida para cada gato é 
sempre a mesma. Faça um programa que receba o peso do saco de ração em gramas e a quantidade de 
ração fornecida para cada gato, calcule e mostre quanto restará de ração no saco após cinco dias.'''
#entrada
peso_saco = int(input("Peso do saco em kilos: "))
racao_gato1 = int(input('Gramas de ração do primeiro gato: '))
racao_gato2 = int(input('Gramas de ração do segundo gato: '))
#processamento
peso_saco = peso_saco * 1000
racao_final = peso_saco - 5 * (racao_gato1 + racao_gato2)
#saida
print('Peso do saco após cinco dias: ',racao_final)