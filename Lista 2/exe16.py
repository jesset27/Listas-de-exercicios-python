'''16. Faça um programa que determine a data cronologicamente maior entre duas datas fornecidas 
pelo usuário. Cada data deve ser composta por três valores inteiros, em que o primeiro representa o 
dia, o segundo, o mês e o terceiro, o ano.'''
ano1 = int(input("Insira o primeiro ano: "))
ano2 = int(input("Insira o segundo ano: "))
mes1 = int(input("Insira o primeiro mês: "))
mes2 = int(input("Insira o segundo: mês: "))
dia1 = int(input("Insira o primeiro dia: "))
dia2 = int(input("Insira o segundo dia: "))
if ano1 > ano2:
    print("A maior data é:",dia1,"-",mes1,"-",ano1)
elif ano2>ano1:
    print("A maior data é:",dia2,"-",mes2,"-",ano2)
elif mes1>mes2:
    print("A maior data é:",dia1,"-",mes1,"-",ano1)
elif mes2>mes1:
    print("A maior data é: ",dia2, "-",mes2,"-",ano2)
elif dia1>dia2:
    print("A maior data é:" "-",dia1,"-",mia1,"-",ano1)
elif dia2>dia1:
    print("A maior data é: ",dia2,"-",mes2,"-",ano2)
else:
    print("As datas são iguais")
