print('====================')
print('10 termos de uma PA ')
print('====================')
t = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
c = 0

while c != 10:
    print(t,end='->')
    t +=r
    c += 1
print('ACABOU')