'''8. A nota final de um estudante é calculada a partir de três notas atribuídas, 
respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. 
A média das três notas mencionadas obedece aos pesos a seguir:
NOTA	PESO
Trabalho de laboratório	2
Avaliação semestral	3
Exame final	5
Faça um programa que receba as três notas, calcule e mostre a média ponderada e o conceito que 
segue a tabela
MÉDIA PONDERADA	CONCEITO
8,0 <= média <= 10	A
7,0 <= média < 8,0	B
6,0 <= média < 7,0	C
5,0 <= média < 6,0	D
0,0 <= média < 5,0	E
media_ponderada = (nota_traballho * 2 + avaliacao_semestral * 3 + exame_final * 5) / 10'''
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 * 2 + n2 * 3 + n3 * 5) / 10
if media >=8.0 and media <=10:
    print("Média final: A ou %,2f" % media)
elif media >= 7.0 and media <8.0:
    print("Média final: B ou %.2f" % media)
elif media >= 6.0 and media <7.0:
    print("Média final: C ou %.2f" % media)
elif media >=5.0 and media <=6.0:
    print("Média final D: ou %.2f" % media)
else: 
    print("Média final: E ou %.2f" % media)
