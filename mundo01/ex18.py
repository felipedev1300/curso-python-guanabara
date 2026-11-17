import math
angulo= float(input('digite um angulo: '))
rad= math.radians(angulo)
print(f'O ângulo de {angulo} tem o seno de {math.sin(rad):.2f}')
print(f'O ângulo de {angulo} tem o cosseno de {math.cos(rad):.2f}')
print(f'O ângulo de {angulo} tem a tangente de {math.tan(rad):.2f}')