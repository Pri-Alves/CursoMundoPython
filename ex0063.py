print('===Sequencia de Fibonacci===')
t = int(input('Quantos termos você quer mostrar? '))
c = 3
t1 = 0
t2 = 1
t3 = 0
print('{}>{}>'.format(t1,t2), end='')
while c <= t:
    t3 = t1 + t2
    print(t3, end='>')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')

