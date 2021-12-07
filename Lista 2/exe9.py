'''9. Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética
 e a mensagem constante na tabela a seguir. Aos alunos que ficaram para exame, calcule e 
 mostre a nota que deverão tirar para serem aprovados, considerando que a média exigida é 6,0.
MÉDIA ARITMÉTICA	MENSAGEM
0 <= média < 3	    Reprovado
3 <= média < 6	    Exame
6 <= média <= 10	Aprovado
'''
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3 ) / 3
nota_exame = 12 - media
if media < 3:
    print("Aluno reprovado")
elif media <= 3 and media < 6:
    print("Aluno necessita de exame")
elif media >= 6 and media <= 10:
    print("Aluno aprovado")
elif media >= 3 and media < 6:  
    print("Você deve tirar a nota %.2f" % nota_exame, " no exame para ser aprovado!")
print("Sua média é: %.2f" % media)