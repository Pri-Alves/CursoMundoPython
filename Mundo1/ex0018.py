import math
n = float(input('Digite o angulo que você deseja: '))
print('o angulo de {} tem o seno de {:.2f}'.format(n,math.sin(math.radians(n))))
print('o angulo de {} tem o COSENO de {:.2f}'.format(n,math.cos(math.radians(n))))
print('o angulo de {} tem a TANGENTE de {:.2f}'.format(n,math.tan(math.radians(n))))