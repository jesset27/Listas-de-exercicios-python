'''25. Faça um programa que receba a altura e peso de uma pessoa. De acordo com a tabela a 
seguir, verifique e mostre a classificação dessa pessoa.
ALTURA	            ATÉ 60	    ENTRE 60 E 90 (INCLUSIVE)	    ACIMA DE 90
Menores que 1,20	A	        D	                            G
De 1,20 a 1,70	    B	        E	                            H
Maiores que 1,70	C	        F	                            I
'''

altura =  float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))
if altura < 1.20:
    if peso <= 60:
        print("Classificação A")
    elif peso > 60 and peso <= 90:
        print("Classificação D")
    elif peso > 90:
        print("Classificação G")
elif altura >= 1.20 and altura <= 1.70:
    if peso <= 60:
        print("Classificação B")
    elif peso > 60 and peso <= 90:
        print("Classificação E")
    elif peso > 90:
        print("Classificação H")
elif altura > 1.70:
    if peso <= 60:
        print("Classificação C")
    elif peso > 60 and peso <= 90:
        print("Classificação F")
    elif peso > 90:
        print("Classificação I")