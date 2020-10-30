import random
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
n = int(input('Em que numero eu Pensei?'))
e = random.randint(0,5)
print('Processando....')
if n == e:
    print('Parabéns! Você conseguiu me vencer')
else:
    print('Ganhei! eu pensei no {} e nao no {}'.format(e,n))