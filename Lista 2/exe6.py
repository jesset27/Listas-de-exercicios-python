'''6. Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio no
 último ano. Faça um algoritmo que leia o saldo médio de um cliente e calcule o valor do
crédito de acordo com a tabela a seguir. Mostre uma mensagem informando o saldo médio e o 
valor do crédito.
Saldo médio
    * de 0 a 200 nenhum crédito
    * de 201 a  400 20% do valor do saldo médio
    * de 401 a  600 30% do valor do saldo médio
    * acima de 601 40% do valor do saldo médio'''
saldo_medio = float(input("Informe o saldo médio: "))
if saldo_medio >=0 and saldo_medio <=200:
    print("Saldo médio: ",saldo_medio)
    print("Recebe um crédito de 0%: ")
elif saldo_medio >=201 and saldo_medio <=400:
    credito = (saldo_medio / 100) * 20
    total = saldo_medio + credito
    print("Saldo Médio: ",total)
    print("Recebe um credito de: %.2f " % credito)
elif saldo_medio >=401 and saldo_medio <=600:
    credito = (saldo_medio / 100) * 30
    total = saldo_medio + credito
    print("Saldo Médio: ",total)
    print("Recebe um credito de: %.2f " % credito)
else: 
    saldo_medio >= 601
    credito = (saldo_medio / 100) * 40
    total = saldo_medio + credito
    print("Saldo médio: ",total)
    print("Recebe um credito de: %.2f " % credito)
