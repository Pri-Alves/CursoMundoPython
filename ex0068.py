from random import randint
print('='*30)
print('Vamos Jogar Par ou Impar')
print('='*30)
s = 0
cont = 0
while True:
    n = int(input('Diga um valor: '))
    e = str(input('Escolha Par ou Impar [P/I]: ')).upper().strip()
    print('-' * 30)
    c = randint(0,10)
    s = n + c
    if s % 2 == 0:
        r = 'PAR'
    else:
        r = 'IMPAR'
    print (f'Voce jogou {n} e o computador {c}. Total de {s}, deu {r}')
    if e == 'P' and r == 'PAR' or e == 'I' and r == 'IMPAR':
        print('Voce VENCEU!!!')
        print('-' * 30)
        print('Vamor jogar novamente...')
        cont += 1
    else:
        print('Voce PERDEU!!!')
        print(f'Game Over! Voce venceu {cont} vezes.')
        break

