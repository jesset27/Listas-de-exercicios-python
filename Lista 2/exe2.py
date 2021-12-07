'''2. Faça um algoritmo que leia o nome e a idade de uma pessoas, verifique se a idade de uma 
pessoa é menor ou maior de idade. Considera-se maior de idade uma pessoa com 18 anos ou mais.
Como saída o algoritmo deve informar o nome e a idade da pessoa e depois uma mensagem se ela
é ou não maior de idade.'''
nome = str(input("Informe o nome: "))
idade = int(input("Informe a idade: "))
print("Nome: ",nome)
print("Idade: ",idade)
if idade <=17:
    print("Menor de idade")
else:
    print("Maior de idade")