from datetime import datetime

'''
print(datetime.now())
 
print(datetime.now().day)

print(datetime.now().month)

print(datetime.now().year)


print(datetime.now().time())

# criar data
lancamento_ap = datetime(2021,5,6)

print(f'Data de Lançamento: {lancamento_ap}')


receberdata = datetime.strptime(input("Quando devemos lançar o app? "),'%d/%m/%Y')
print(type(receberdata))

contagem = receberdata - datetime.now()
print(contagem)'''


aniversário = datetime.strptime(input("Diga o dia mes e ano do seu aniversário"),'%d/%m/%Y')
calcular = aniversário - datetime.now()
print(calcular)
