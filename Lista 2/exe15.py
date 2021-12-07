'''15. Faça um programa que mostre a data e a hora do sistema nos seguintes 
formatos: dia/mês/ano – mês por extenso e hora:minuto.
Observação: from carrega um módulo/biblioteca da linguagem Python e o import é usado para 
informar qual objeto desta biblioteca queremos importar/carregar no nosso programa'''
from datetime import datetime
hoje = datetime.now()
if hoje.month == 1:
    print(hoje.day,"/","Janeiro","/",hoje.year)
elif hoje.month == 2:
    print(hoje.day,"/","Feveiro","/",hoje.year)
elif hoje.month == 3:
    print(hoje.day,"/","Março","/",hoje.year)
elif hoje.month == 4:
    print(hoje.day,"/","Abril","/",hoje.year)
elif hoje.month == 5:
    print(hoje.day,"/","Maio","/",hoje.year)
elif hoje.month == 6:
    print(hoje.day,"/","Junho","/",hoje.year)
elif hoje.month == 7:
    print(hoje.day,"/","Julho","/",hoje.year)
elif hoje.month == 8:
    print(hoje.day,"/","Agosto","/",hoje.year)
elif hoje.month == 9:
    print(hoje.day,"/","Setembro","/",hoje.year)
elif hoje.month == 10:
    print(hoje.day,"/","Outubro","/",hoje.year)
elif hoje.month == 11:
    print(hoje.day,"/","Novembro","/",hoje.year)
elif hoje.month == 12:
    print(hoje.day,"/","Dezembro","/",hoje.year)
print(hoje.hour,":",hoje.minute)