n = int(input('Digite um numero: '))
cont=0
for c in range(1,n+1):
    if n % c == 0:
        cont += 1
        print('\33[33m', end='')
    else:
        print('\33[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n,cont))
if cont <= 2:
    print('E por isso ele é Primo!')
else:
    print('E por isso ele não é Primo!')

