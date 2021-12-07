'''11. Faça um programa que receba três números e mostre-os em ordem crescente. 
Suponha que o usuário digitará três números diferentes.'''
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))
if n1 < n2 and n1 < n3:
    if n2 < n3:
        print("A ordem crescente é:",n1,"-",n2,"-",n3)
    else:
        print("A ordem crescente é:",n1,"-",n3,"-",n2)
if n2 < n1 and n2 < n3:
    if n1 < n3:
        print("A ordem crescente é:",n1,"-",n2,"-",n3)
    else:
        print("A ordem crescente é:",n2,"-",n3,"-",n1)
if n3 < n1 and n3 < n2:
    if n1<n2:
        print("A ordem crescente é:", n3,"-",n1,"-",n2)
    else:
        print("A ordem crescente é",n3,"-",n2,"-",n1)
