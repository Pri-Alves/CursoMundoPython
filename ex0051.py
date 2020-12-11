print('====================')
print('10 termos de uma PA ')
print('====================')
t = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
for c in range(0,10):
    print(t,end='->')
    t +=r
print('ACABOU')


