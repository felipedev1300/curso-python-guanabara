preço = float(input('qual o preço do produto? '))
desconto = preço * 0.05
final= preço - desconto
print (f'se o preço do produto é ${preço} com 5% de desconto fica ${final:.2f}')