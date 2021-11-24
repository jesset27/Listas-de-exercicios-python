'''14. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a idade dessa pessoa;
quantos anos ela terá em 2050'''

#entrada
anonascimento = int(input( 'Ano de nascimento: '))
anoatual = int(input('Ano atual: '))
#processamento
idadeatual = anoatual - anonascimento
ano2050 = 2050 - anonascimento
print('Idade atual:',idadeatual)
print('Idade em 2050:',ano2050)