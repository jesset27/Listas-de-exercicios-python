'''24. Dados três valores X, Y e Z, verifique se eles podem ser os comprimentos dos lados de um 
triângulo e, se forem, verifique se é um triângulo equilátero, isósceles ou escaleno. Se eles não
formarem um triângulo, escreva uma mensagem.
Considere que:
    o comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados;
    chama-se equilátero o triângulo que tem três lados iguais;
    denomina-se isósceles o triângulo que tem o comprimento de dois lados iguais;
    recebe o nome de escaleno o triângulo que tem os três lados diferentes.'''

x = float(input("Digite a medida 1: "))
y = float(input("Digite a medida 2: "))
z = float(input("Digite a medida 3: "))
if x < y + z and y < x + z and z < x + y:
    if x == y and y == z:
        print("Triângulo Equilátero")
    elif x == y or x == z or y == z:
        print("Triângulo Isósceles")
    elif x != y and x != z and y != z:
        print("Triângulo Escaleno")
else:
    print("Essas medidas não formam um triângulo")