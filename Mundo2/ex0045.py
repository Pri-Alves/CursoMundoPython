from random import randint

print('Suas Opções:')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
e = int(input('Qual é a sua jogada? '))
c = randint(0,2)
l = ['Pedra', 'Papel','Tesoura']
print('JOKENPO!!!')
print('=-=-=-=-=-=-=-=-=-=-=')
print('Computador Jogou {}'.format(l[c]))
print('Jogador jogou {}'.format(l[e]))
print('=-=-=-=-=-=-=-=-=-=-=')
if e == 0 and c == 2 or e == 1 and c == 0 or e == 2 and c == 1:
    print("JOGADOR VENCE!!")
elif c == 0 and e == 2 or c == 1 and e == 0 or c == 2 and e == 1:
    print('COMPUTADOR VENCE!!')


