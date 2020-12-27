print('====================')
print('10 termos de uma PA ')
print('====================')
t = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
c = 0
tm = 10

while tm != 0:
    while c != tm:
        print(t,end='->')
        t +=r
        c += 1
    print('PAUSA')
    tm = int(input('Quantos termos você quer ver a mais? '))
    if tm != 0:
        c = 0
else:
    print('ACABOU')