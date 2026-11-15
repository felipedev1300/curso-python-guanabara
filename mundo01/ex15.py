dias= float(input('você alugou o carro por quantos dias? '))
km= float(input('quantos km você rodou com o carro? '))
aluguel= dias * 60
Km= dias * 0.15
print(f'o total a se pagar é {aluguel + Km:.2f}')