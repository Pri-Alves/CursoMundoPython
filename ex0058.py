import random
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
n = int(input('Em que numero eu Pensei?'))
e = random.randint(0,10)
cont = 1
while not e == n:
    cont += 1
    if e > n:
        print('Mais...tente mais uma vez')
        n = int(input('Em que numero eu Pensei?'))
    elif n > e:
        print('Menos...tente mais uma vez')
        n = int(input('Em que numero eu Pensei?'))
print('Acertou com {} tentativas. Parabens!'.format(cont))